from django.shortcuts import render,redirect
from .models import Auteur, Question, Reponse, Like
from .forms import QuestionForm
from django.db.models import Count
from django.db.models import Q



def home(request):
    questions = Question.objects.all().order_by('-date')
    context = {'questions':questions}
    return render(request, 'home.html', context)


def ask_question(request):
    if request.method == 'POST':
        new_question = Question.objects.create(
            question = request.POST.get('question'),
            auteur = request.POST.get('auteur'),
            date = request.POST.get('time')
        )
        return redirect('home')
    return render(request, 'question.html')


def answer(request, i_question):
    if request.method =='POST':
        reponse = Reponse.objects.create(
            body = request.POST.get('reponse'),
            auteur = request.POST.get('auteur'),
            question = Question.objects.get(question = i_question)

        )
        return redirect('home')
    context = {}
    return render(request, 'reponse.html', context)



def afficher(request,pk):
    reponses = Reponse.objects.prefetch_related('likes').filter(question = pk)
    context = {'reponses':reponses}
    return render(request, 'afficher.html', context)


def j_aime(request,i_body):
    reponse = Reponse.objects.get(body = i_body)
    like, created = Like.objects.get_or_create(reponse = reponse)
    like.likes +=1
    like.save()
    return redirect(request.META.get('HTTP_REFERER'))


def je_n_aime_pas(request,i_body):
    reponse = Reponse.objects.get(body = i_body)
    like, created = Like.objects.get_or_create(reponse = reponse)
    like.dislikes += 1
    like.save()
    return redirect(request.META.get('HTTP_REFERER'))



