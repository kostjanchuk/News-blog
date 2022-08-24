from django.shortcuts import render, redirect
from django.views.generic import ListView
# from vacancies.models import Vacancy
# from account.models import Profile

from news.models import News



class FavoritesList(ListView):
    model = News
    template_name = 'favorites/favorites-list.html'
    context_object_name = 'news'
    allow_empty = True
    paginate_by = 5

    def get_queryset(self):
        # if self.request.session.get('_auth_user_id'):
        #     if not self.request.session.get('favorites'):
        #         profile = Profile.objects.get(user__id=self.request.session['_auth_user_id'])
        #         self.request.session['favorites'] = [item.id for item in list(profile.favorites.all())]
        #     return Vacancy.objects.filter(id__in=self.request.session['favorites'])
        #
        # elif self.request.session.get('favorites'):
        #     return Vacancy.objects.filter(id__in=self.request.session['favorites'])
        # else:
        #     return Vacancy.objects.none()

        if not self.request.session.get('favorites'):
            return News.objects.none()
        else:
            print(News.objects.filter(id__in=self.request.session['favorites']))
            return News.objects.filter(id__in=self.request.session['favorites']).select_related('category')


def add_to_favorites(request, id):
    previous_url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        item_exist = next((item for item in request.session['favorites'] if item == int(id)), False)

        if not item_exist:
            request.session['favorites'].append(int(id))
            request.session.modified = True
    News.objects.filter(id=id).update(favorites=True)
    return redirect(previous_url)


def remove_from_favorites(request, id):
    previous_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item == int(id) :
                request.session['favorites'].remove(item)

        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True

    return redirect(previous_url)


def delete_favorites(request):
    previous_url = request.META.get('HTTP_REFERER')
    if request.session.get('favorites'):
        del request.session['favorites']
    return redirect(previous_url)
