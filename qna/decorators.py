from django.contrib import messages
from django.shortcuts import redirect


# superuser 권한 데코레이터
def superuser_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            messages.info(request, '접근 권한이 없습니다.')
            return redirect('home')
    return wrap
