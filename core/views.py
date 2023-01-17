from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'core/head.html')


@login_required
def mypage(request):
    return render(request, 'core/mypage.html')


@login_required
def custom(request):
    return render(request, 'core/custom.html')