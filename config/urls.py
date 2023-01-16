from django.contrib import admin
from django.urls import path, include

import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('f_login/', accounts.views.home, name='home'),
    path('f_logout/', accounts.views.home, name='home'),
    path('f_register/', accounts.views.home, name='home'),
]
