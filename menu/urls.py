# menu/urls.py
from django.shortcuts import render
from django.urls import path
from .views import index, home_view

urlpatterns = [
    path('', index, name='index'),
    path('home/', home_view, name='home_page'),
    path('menu/', lambda request: render(request, 'menu/menu.html'), name='menu_page'),
]
