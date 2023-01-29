from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from accounts.ecampus import ecampus, information
from accounts.forms import UserForm
from accounts.models import Year, Department, Profile, LoginHistory


def agree(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():     # 학번 중복 검사
            messages.error(request, '⚠️ 이미 가입된 학번입니다.')
            return redirect('accounts:agree')

        context = information(ecampus(username, password))
        if context:
            if Year.objects.filter(year=username[:4]) and Department.objects.filter(name=context['department']):
                context['id'] = username
                request.session['context'] = context
                return redirect('accounts:register')

            messages.error(request, '⚠️ 서비스에서 지원하지 않는 학과와 학번 입니다.')
            return redirect('accounts:agree')
        messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
        return redirect('accounts:agree')
    departments = Department.objects.all()
    dept_num = departments.count()
    return render(request, 'accounts/agree.html', {'departments': departments, 'dept_num': dept_num})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            LoginHistory.objects.create(user=user)
            return redirect('core:mypage')
        if User.objects.filter(username=username):
            messages.error(request, '⚠️ 비밀번호를 확인하세요.')
        else:
            messages.error(request, '⚠️ 가입되지 않은 학번입니다.')
        redirect('accounts:login')
    return render(request, 'accounts/login.html')


def register(request):
    context = request.session.get('context')

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            year = Year.objects.filter(year=context['id'][:4]).first()
            department = Department.objects.filter(name=context['department']).first()
            if year and department:  # 지원하는 학과와 학번인지 확인
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                Profile.objects.create(user=user, year=year, department=department, name=context['name'])
                auth_login(request, user)  # 로그인
                LoginHistory.objects.create(user=user)
                return redirect('core:mypage')
            messages.error(request, '⚠️ 서비스에서 지원하지 않는 학과와 학번 입니다.')
            return redirect('accounts:agree')
        messages.error(request, form.errors['password2'][0])
        return redirect('accounts:register')
    form = UserForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)


def change_pw(request):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            user = get_object_or_404(User, username=request.POST["id"])
        if request.POST["password1"] == request.POST["password2"]:
            user.set_password(request.POST["password1"])
            user.save()
            messages.error(request, '비밀번호가 변경되었습니다.')
        else:
            messages.error("⚠️ 비밀번호가 일치하지 않습니다.")
    return redirect('core:mypage')


def update(request):
    if request.method == "POST":
        password = request.POST["password"]
        context = information(ecampus(request.user.username, password))
        if context:
            department = Department.objects.filter(name=context['department'])
            if department:
                Profile.objects.filter(user=request.user).update(name=context['name'], department=department.first())
                messages.error(request, '회원 정보가 업데이트 되었습니다.')
                return redirect('core:mypage')
            messages.error(request, '⚠️ 서비스에서 지원하지 않는 학과와 학번 입니다.')
        messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
    return redirect('core:mypage')

def find_pw(request):
    if request.method == "POST":
        # ecampus 존재하면
        username = request.POST["id"]
        password = request.POST["password1"]
        if not User.objects.filter(username=username):
            messages.error(request, '⚠️ 가입되지 않은 학번입니다.')
            return redirect('accounts:login')
        context = information(ecampus(username, password))
        if context:
            return render(request, 'accounts/changePW.html', {'username': username})
    messages.error(request, '⚠️ 샘물 포털 ID/PW를 다시 확인하세요! (Caps Lock 확인)')
    return redirect('accounts:login')
