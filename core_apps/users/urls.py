from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/",views.login,name="user-login"),
    path("register/",views.register,name="user-register"),
    path("logout/",views.register,name="user-logout"),
]
