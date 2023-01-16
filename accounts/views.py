from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm


def home(request):
    return render(request, 'core/head.html')


def agree(request):
    return render(request, 'accounts/agree.html')


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})


def change_pw(request):
    return render(request, 'accounts/changePW.html')