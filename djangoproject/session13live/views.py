from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Answer, Question

# Create your views here.


def vote(request, answer_pk=None):
    if answer_pk and request.user.is_authenticated:
        answer = Answer.objects.get(pk=answer_pk)
        answer.number_of_votes = answer.number_of_votes + 1
        answer.save()
    return render(request, 'vote.html', {"questions": Question.objects.all(),
                                         "user": request.user})


@login_required
def new_question(request):
    if request.method == 'POST':
        question = Question(text=request.POST['question_text'])
        question.save()
    return render(request, 'new_question.html')

@login_required
def new_answer(request):
    if request.method == 'POST':
        question_pk = request.POST['question_pk']
        answer_text = request.POST['answer_text']
        question = Question.objects.get(pk=question_pk)
        answer = Answer(question=question, text=answer_text)
        answer.save()
    return render(request, 'new_answer.html', {"questions": Question.objects.all()})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
