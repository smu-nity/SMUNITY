from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('auth', views.authenticate, name='authenticate'),
    path('userinfo', views.userinfo, name='userinfo'),
]
