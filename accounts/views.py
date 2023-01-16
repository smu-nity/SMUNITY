from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# django를 활용하여 입력한 id와 password를 가지는 user 생성
# password1과 password2를 확인하여 둘이 일치하면 해당 user를 만들어줌
def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request,user)
            return redirect('home')
    return render(request,'signup.html')

# auth.authenticate를 이용해 request한 user정보를 가진 user를 인증하여 로그인시켜
# home으로 보냄, 아이디나 비밀번호가 틀린 경우 에러
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'signup.html')


def home(request):
    return render(request, 'core/head.html')

def agree(request):
    return render(request, 'accounts/agree.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def change_pw(request):
    return render(request, 'accounts/changePW.html')