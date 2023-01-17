from django.contrib.auth import get_user_model
from django.shortcuts import render

from accounts.models import Profile
from core.models import Course
from graduations.models import Subject


def home(request):
    return render(request, 'core/head.html')


def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    cg_list = Course.objects.filter(user=user)
    return render(request, 'core/mypage.html', {'user': user, 'profile': profile, 'cg_list': cg_list})


