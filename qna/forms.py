from django import forms
from qna.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'anonymous']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
