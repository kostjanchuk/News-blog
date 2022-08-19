from django.urls import path
from .views import HomeNews, NewsByCategory, DetailNews, CreateNews, SendMessage

# index, list_of_categories,detail_news,add_news,
urlpatterns = [
    # path('', index, name='home'),
    # path('categories/<int:pk>/', list_of_categories, name='category'),
    # path('news/<int:pk>/', detail_news, name ='detail_news'),
    # path('add_news/', add_news, name='add_news'),
    path('', HomeNews.as_view(), name='home'),
    path('categories/<int:pk>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', DetailNews.as_view(), name='detail_news'),
    path('add_news/', CreateNews.as_view(extra_context={'title': 'Add news'}), name='add_news'),
    path('send_message/', SendMessage.as_view(), name='send_message')
]
