from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views import View
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.contrib import messages
from .models import Article
from .forms import ArticleForm


class IndexView(View):

    title = 'Статьи'
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        query =  request.GET.get('query', '')
        articles = Article.objects.filter(Q(name__icontains=query))
        return render(request, self.template_name, {'articles': articles})
        

class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/article_detail.html', {'article': article})


class ArticleCreateView(View):
    
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        article_name = form.data['name']
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,  f"Articele {article_name} crested")
            return redirect('articles_index')
        return render(request, 'article/create.html', {'form': form})


class ArticleUpdateView(View):
    
    def get(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/create.html', {'form': form, 'id':article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,  f"Articele {article.name} updated!!")
            return redirect('articles_index')
        return render(request, 'article/create.html', {'form': form})


class ArticleDeleteView(View):
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles_index')
