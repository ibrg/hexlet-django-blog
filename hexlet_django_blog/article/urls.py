from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:id>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/', views.ArticleView.as_view(), name='article_detail'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create')
]
