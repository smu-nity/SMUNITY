from django.contrib import admin
from qna.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['subject', 'author', 'anonymous', 'create_date', 'modify_date']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question__subject']
    list_display = ['question', 'author', 'create_date', 'modify_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
