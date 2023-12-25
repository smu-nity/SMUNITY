from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from qna.decorators import superuser_required
from qna.forms import QuestionForm, AnswerForm
from qna.models import Question, Answer


def question_list(request):
    ql = Question.objects.all().order_by('-create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(ql, 5)
    page_obj = paginator.get_page(page)
    return render(request, 'qna/question_list.html', {'question_list': page_obj})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    answers = Answer.objects.filter(question=question)
    if answers:
        context['answer'] = answers.first()
    return render(request, 'qna/question_detail.html', context)


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('qna:question_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'qna/question_form.html', context)


@login_required
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('qna:question_detail', question_id=question.pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.modify_date = timezone.now()
            petition.save()
            return redirect('qna:question_detail', question_id=question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'qna/question_form.html', context)


@login_required
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('qna:question_detail', question_id=question.id)
    question.delete()
    return redirect('qna:question_list')


@superuser_required
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if Answer.objects.filter(question=question):
        messages.error(request, '이미 답변한 질문 입니다.')
        return redirect('qna:question_detail', question_id=question.pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('qna:question_detail', question_id=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'qna/answer_form.html', {'form': form, 'question': question})


@superuser_required
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('qna:question_detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'qna/answer_form.html', {'form': form, 'question': answer.question})


@superuser_required
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('qna:question_detail', question_id=answer.question.id)


def terms(request):
    return render(request, 'qna/terms.html')


def privacy(request):
    return render(request, 'qna/privacy.html')
