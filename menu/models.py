# menu/models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', default=None)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', default=None)

