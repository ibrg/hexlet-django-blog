from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    title = 'Articles'
    return render(request, 'article/article.html', {'title': title})
