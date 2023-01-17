from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Course

def home(request):
    return render(request, 'core/head.html')


@login_required
def mypage(request):
    return render(request, 'core/mypage.html')


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
