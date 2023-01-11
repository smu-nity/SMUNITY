from django.shortcuts import render


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