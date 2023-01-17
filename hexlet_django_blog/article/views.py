from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods
from .models import Article


def index(request, tags, article_id):
    context = {'tags': tags, 'article_id': article_id}
    return render(request, 'article/article_detail.html', context)


class ArticleView(View):

    title = 'Articles'
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {
            'title': self.title,
            'articles': Article.objects.all()
            })


@require_http_methods(['GET'])
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    if article:
        return render(request, 'article/article_detail.html', {'article': article})
    else:
        raise Http404('Not found')
    