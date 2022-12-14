from django import template
from news.models import Category, News

from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.filter(news__is_published=True).annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories}