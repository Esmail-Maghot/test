from . import views
from django.urls import path

urlpatterns =[
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    ]