from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import NewsForm, ContactForm
from .models import News, Category
from django.urls import reverse, reverse_lazy
from .utils import MixinNews
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail


class HomeNews(MixinNews, ListView):

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MixinNews, ListView):

    def get_queryset(self):
        return News.objects.filter(is_published=True).filter(category_id=self.kwargs['pk']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['pk'])
        return context


class DetailNews(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    select_related = 'category'
    login_url = '/admin'


class SendMessage(FormView):
    form_class = ContactForm
    template_name = 'news/contact.html'

    def form_valid(self, form):
        mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                         'kostjanchuk@gmail.com', ['kostjanchuk@gmail.com'], fail_silently=True)
        if mail:
            messages.success(self.request, 'Email sent successfully')
            return redirect('home')
        return super(SendMessage, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Email sending error')
        return super(SendMessage, self).form_invalid(form)


# def index(request):
#     context = {'news': News.objects.all(),
#                'title': 'News',ш
#                # 'url': reverse('list', kwargs={'pk': 2})
#                }
#     return render(request, 'news/index.html', context=context)
#
#
# def list_of_categories(request, pk):
#     context = {
#         'news': News.objects.filter(category_id=pk),
#         'title': 'News',
#     }
#     return render(request, 'news/index.html', context=context)


# def detail_news(request, pk):
#     context = {
#         'news': get_object_or_404(News, pk=pk)
#     }
#     return render(request, 'news/detail_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news=News.objects.create(**form.cleaned_data)
#             # return redirect(news.get_absolute_url())
#             news = form.save()
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
