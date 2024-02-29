# menu/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'menu/index.html')


def home_view(request):
    return render(request, 'home.html')


def menu_view(request):
    return render(request, 'menu.html')