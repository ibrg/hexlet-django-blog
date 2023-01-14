from django.shortcuts import render


def index(request):
    context = {'who': 'World'}
    return render(request, 'index.html', context)


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', context={'tags': tags})
