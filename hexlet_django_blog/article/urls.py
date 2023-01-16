from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='articles'),
    path('<str:tags>/<int:article_id>', views.index, name='article'),
    path('<int:article_id>/', views.article, name='article_detail')
]
