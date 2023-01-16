from django.shortcuts import render
from django.views import View



articles = [
    {'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'title': '"5 min recepies"', 'author': 'H. Lector'},
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