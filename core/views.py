import datetime
import json
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from sangmyung_univ_auth import completed_courses

from accounts.models import Profile, Department, Statistics
from config.settings import CULTURES_1, CULTURES_2, CULTURES_DIC1, CULTURES_DIC2
from core.models import Course
from graduations.models import Subject, Major
import logging

logger = logging.getLogger('smunity')

def home(request):
    departments = Department.objects.filter(url__isnull=False)
    dept_num, today = departments.count(), datetime.date.today()
    st, _ = Statistics.objects.get_or_create(date=today)
    visit_total = Statistics.objects.aggregate(Sum('visit_count'))['visit_count__sum']
    user_num = format(Profile.objects.all().count(), ',')
    visit_total, visit_today = format(visit_total, ','), format(st.visit_count, ',')
    response = render(request, 'core/head.html', {'departments': departments, 'dept_num': dept_num, 'user_num': user_num, 'visit_total': visit_total, 'visit_today': visit_today})
    if request.COOKIES.get('is_visit') is None:
        response.set_cookie('is_visit', 'visited', 60*30)
        st.visit_count += 1
        st.save()
    return response


def team(request):
    return render(request, 'core/team.html')


@login_required
def mypage(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    courses = Course.objects.filter(user=user).order_by('-pk')
    return render(request, 'core/mypage.html', {'user': user, 'profile': profile, 'courses': courses, 'short': courses[:5]})


@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.user != course.user or not course.custom:
        messages.error(request, '⚠️삭제권한이 없습니다.')
        return redirect('core:custom')
    course.delete()
    return redirect('core:custom')


# 기이수과목 업로드
@login_required
def course_update(request):
    if request.method == "POST":
        password = request.POST["password"]
        result = completed_courses(request.user.username, password)
        if result.is_auth:
            # 추가 전 기존 데이터 삭제
            courses = Course.objects.filter(user=request.user)
            if courses.exists():
                courses.delete()
            # 기이수과목 추가
            subjects = result.body
            for sub in subjects:
                subject, _ = Subject.objects.get_or_create(number=sub['SBJ_NO'], defaults={'name': sub['SBJ_NM'], 'credit': sub['CDT'], 'dept': '커스텀', 'type': sub['CMP_DIV_NM']})
                domain = sub['CULT_ARA_NM']
                if domain == '*':
                    domain = None
                if sub['GRD_NM'] != 'F':
                    if not Course.objects.filter(user=request.user, subject=subject):
                        Course.objects.create(user=request.user, subject=subject, year=sub['SCH_YEAR'], semester=sub['SMT_NM'], credit=sub['CDT'], type=sub['CMP_DIV_NM'], domain=domain)
            messages.error(request, '기이수과목이 업데이트 되었습니다.')
            return redirect('core:result')
        messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
    return redirect('core:mypage')


# har 파일 업로드
@login_required
def course_update_har(request):
    file, success = request.FILES['file'], False

    # har 파일인지 검사
    if file.name[-3:] != 'har':
        messages.error(request, '⚠️ 잘못된 파일 형식입니다. 확장자가 har인 파일을 올려주세요. ')
        return redirect('core:mypage')

    # 추가 전 기존 데이터 삭제
    courses = Course.objects.filter(user=request.user)
    if courses.exists():
        courses.delete()

    # 기이수과목 추가
    response = json.loads(file.read())['log']['entries']
    for res in response:
        try:
            subjects = json.loads(res['response']['content']['text'])['dsRecMattList']
            for sub in subjects:
                subject, _ = Subject.objects.get_or_create(number=sub['SBJ_NO'], defaults={'name': sub['SBJ_NM'], 'credit': sub['CDT'], 'dept': '커스텀', 'type': sub['CMP_DIV_NM']})
                domain = sub['CULT_ARA_NM']
                if domain == '*':
                    domain = None
                if sub['GRD_NM'] != 'F':
                    if not Course.objects.filter(user=request.user, subject=subject):
                        Course.objects.create(user=request.user, subject=subject, year=sub['SCH_YEAR'], semester=sub['SMT_NM'], credit=sub['CDT'], type=sub['CMP_DIV_NM'], domain=domain)
            success = True
        except:
            logger.error(res)
    if success:
        messages.error(request, '기이수과목이 업데이트 되었습니다.')
    else:
        messages.error(request, '⚠️ 파일 내용이 다릅니다! 다운로드 방법을 확인해주세요.')
    return redirect('core:mypage')


# 엑셀파일 업로드
@login_required
def course_update_excel(request):
    file = request.FILES['file']

    # 엑셀파일인지 검사
    if file.name[-4:] != 'xlsx':
        messages.error(request, '⚠️ 잘못된 파일 형식입니다. 확장자가 xlsx인 파일을 올려주세요. ')
        return redirect('core:mypage')

    # 추가 전 기존 데이터 삭제
    courses = Course.objects.filter(user=request.user)
    if courses.exists():
        courses.delete()

    # 기이수과목 추가
    try:
        df = pd.read_excel(file)
        for _, item in df.iterrows():
            if item[0].isnumeric():
                subject = Subject.objects.get(number=item[2])
                domain = item[19]
                if domain == '*':
                    domain = None
                if item[9] != 'F':
                    if not Course.objects.filter(user=request.user, subject=subject):
                        Course.objects.create(user=request.user, subject=subject, year=item[0], semester=item[1], credit=item[7], type=item[6], domain=domain)
    except:
        messages.error(request, '⚠️ 엑셀 내용이 다릅니다! 수정하지 않은 엑셀파일을 올려주세요.')
        return redirect('core:mypage')
    messages.error(request, '기이수과목이 업데이트 되었습니다.')
    return redirect('core:mypage')


@login_required
def result(request):
    profile = get_object_or_404(Profile, user=request.user)
    courses = Course.objects.filter(user=request.user)
    cnt, check = 0, int(profile.year.year) < 2020
    culture_b = CULTURES_1 if check else CULTURES_2
    culture_dic = CULTURES_DIC1 if check else CULTURES_DIC2
    for culture, dics in zip(culture_b, culture_dic):
        q = Q()
        for key in dics:
            q |= Q(domain__contains=key)
        course = Course.objects.filter(q)
        culture['course'] = course
        if course:
            cnt += 1

    context = {
        'profile': profile, 'major_i': Major.objects.filter(department=profile.department, type='1전심').exclude(subject_id__in=courses.values_list('subject', flat=True)),
        'major_s': Major.objects.filter(department=profile.department, type='1전선').exclude(subject_id__in=courses.values_list('subject', flat=True)), 'culture_b': culture_b, 'culture_cnt': cnt,
        'subjects_all': profile.subjects_all(), 'subjects_major_i': profile.subjects_major_i(), 'subjects_major_s': profile.subjects_major_s(), 'subjects_culture': profile.subjects_culture,
        'subjects_culture_e': profile.subjects_culture_e(), 'subjects_culture_s': profile.subjects_culture_s()
    }
    return render(request, 'core/result.html', context)


def member_del(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            messages.error(request, '회원 탈퇴 되었습니다.')
            return redirect('home')
    messages.error(request, '⚠️ 비밀번호가 일치하지 않습니다.')
    return redirect('core:mypage')
