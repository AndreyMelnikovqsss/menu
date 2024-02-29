# ваш_проект/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    # Добавьте другие URL-маршруты по необходимости
]
