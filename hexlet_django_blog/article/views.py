from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views import View
from django.views.decorators.http import require_http_methods
from .models import Article


def index(request, tags, article_id):
    context = {'tags': tags, 'article_id': article_id}
    return render(request, 'article/article_detail.html', context)


class IndexView(View):

    title = 'Статьи'
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {
            'title': self.title,
            'articles': get_list_or_404(Article)
            })


class ArticleView(View):
    
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'article/article_detail.html', {'article': article})

    