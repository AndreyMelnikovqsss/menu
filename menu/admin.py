#Email address: address@gmail.com
#password: 1
# menu/admin.py
from django.contrib import admin
from .models import Menu, MenuItem
from .forms import MenuItemAdminForm


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'named_url', 'parent', 'menu']
    form = MenuItemAdminForm


admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)
