from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('articles_index'))


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html')
