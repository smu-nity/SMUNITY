from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/head.html')

def agree(request):
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
    if request.method == 'POST':
        user = User.object.create_user(
            username=request.POST['id'], password=request.POST['pw'])
        auth_login(request, user)
        return redirect('')
    return render(request, 'accounts/register.html')

def change_pw(request):
    return render(request, 'accounts/changePW.html')