import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from core.models import Course
from graduations.models import Subject


def home(request):
    return render(request, 'core/head.html')


@login_required
def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    courses = Course.objects.filter(user=user)
    return render(request, 'core/mypage.html', {'user': user, 'profile': profile, 'courses': courses})


@login_required
def custom(request):
    courses = Course.objects.filter(user=request.user)
    context = {'courses':courses}
    return render(request, 'core/custom.html', context)

@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.user != course.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('core:custom', course_id=course.subject.number)
    course.delete()
    return redirect('core:custom')

# 기이수과목 업로드
@login_required
def course_update(request):
    excel = request.FILES['excel']

    # 엑셀파일인지 검사
    if excel.name[-4:] != 'xlsx':
        messages.error(request, '⚠️ 잘못된 파일 형식입니다. 확장자가 xlsx인 파일을 올려주세요. ')
        return redirect('core:mypage')

    # 추가 전 기존 데이터 삭제
    courses = Course.objects.filter(user=request.user)
    if courses.exists():
        courses.delete()

    # 기이수과목 추가
    try:
        df = pd.read_excel(excel)
        for _, item in df.iterrows():
            if item[0].isnumeric():
                subject = Subject.objects.get(number=item[2])
                domain = item[19]
                if domain == '*':
                    domain = None
                Course.objects.create(user=request.user, subject=subject, year=item[0], semester=item[1], credit=item[7], type=item[6], domain=domain)
    except:
        messages.error(request, '⚠️ 엑셀 내용이 다릅니다! 수정하지 않은 엑셀파일을 올려주세요.')
        return redirect('core:mypage')
    messages.success(request, '업데이트성공')
    return redirect('core:mypage')

@login_required
def result(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'core/result.html', {'profile': profile})
