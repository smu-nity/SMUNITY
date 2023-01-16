from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.ecampus import ecampus, information
from accounts.models import Year, Department


def home(request):
    return render(request, 'core/head.html')


def agree(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():     # 학번 중복 검사
            messages.error(request, '⚠️ 이미 가입된 학번입니다!')
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
    return render(request, 'accounts/agree.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            if User.objects.filter(username=username):
                messages.error(request, '⚠️ 비밀번호를 확인하세요.')
            else:
                messages.error(request, '⚠️ 가입되지 않은 학번입니다.')
            redirect('accounts:login')
    return render(request, 'accounts/login.html')


def register(request):
    context = request.session.get('context')
    print(context)
    return render(request, 'accounts/register.html')


def change_pw(request):
    return render(request, 'accounts/changePW.html')
