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
            return render(request, 'accounts/login.html', {'error':'id or pw is incorrect'})
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