from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:article_id>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<str:tags>/<int:article_id>', views.index, name='article'),
    path('<int:article_id>/', views.ArticleView.as_view(), name='article_detail'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create')
]
