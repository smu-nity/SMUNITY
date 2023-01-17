from django.shortcuts import render

def home(request):
    return render(request, 'core/head.html')


def mypage(request):
    return render(request, 'core/mypage.html')


def custom(request):
    return render(request, 'core/custom.html')