from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('custom/', views.custom, name='custom'),
]
