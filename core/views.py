from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import Profile
from core.models import Course
from graduations.models import Subject


def home(request):
    return render(request, 'core/head.html')


@login_required
def mypage(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    cg_list = Course.objects.filter(user=user)
    return render(request, 'core/mypage.html', {'user': user, 'profile': profile, 'cg_list': cg_list})


@login_required
def custom(request):
    courses = Course.objects.filter(user=request.user)
    context = {'courses':courses}
    return render(request, 'core/custom.html', context)

@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.user != course.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('core:custom', course_id=course.subject.number)
    course.delete()
    return redirect('core:custom')
