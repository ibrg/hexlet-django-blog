from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    list_filter = (('timestamp', DateFieldListFilter),)
    search_fields = ['name', 'body']
    