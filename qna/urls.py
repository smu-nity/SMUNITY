from django.urls import path

from qna import views

app_name = 'qna'

urlpatterns = [
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/create/', views.question_create, name='question_create'),
    path('questions/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('questions/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
