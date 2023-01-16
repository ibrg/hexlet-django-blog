from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods


articles = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]


def index(request, tags, article_id):
    context = {'tags': tags, 'article_id': article_id}
    return render(request, 'article/article_detail.html', context)


class ArticleView(View):

    title = 'Articles'
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {
            'title': self.title,
            'articles': articles
            })


@require_http_methods(['GET'])
def article(request, article_id):
    article = [article for article in articles if article['id'] == article_id]
    if article:
        return render(request, 'article/article_detail.html', {'article': article})
    else:
        raise Http404('Not found')
    