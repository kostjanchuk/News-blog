from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.views.generic.base import View

from .forms import UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail


class UserRegister(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'You have successfully registered')
        return super(UserRegister, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Register error')
        return super(UserRegister, self).form_invalid(form)


class UserLogin(FormView):
    template_name = 'users/login.html'
    success_url = '/'
    form_class = UserLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(UserLogin, self).form_valid(form)


class UserLogout(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('home')

# def user_logout(request):
#     logout(request)
#     return redirect('home')


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'users/login.html', {"form": form})


# def user_register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request, user)
#             messages.success(request, 'You have successfully registered')
#
#             return redirect('home')
#
#         else:
#             messages.error(request, 'Registration error')
#
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


