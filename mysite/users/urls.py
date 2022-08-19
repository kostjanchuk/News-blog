from django.urls import path
from .views import  UserLogin, UserRegister, UserLogout
# user_login,  user_register, ,user_logout
urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', UserLogin.as_view(), name = 'login'),
    # path('logout/', user_logout, name='logout'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
    # path('register/', user_register, name='register'),
]
