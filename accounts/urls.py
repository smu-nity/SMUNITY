from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('agree/', views.agree, name='agree'),
    path('change/', views.change_pw, name='change'),
    path('update/', views.update, name='update'),
    path('update/dept/<int:pk>/', views.change_dept, name='chage_dept'),
    path('find/', views.find_pw, name='find'),
]
