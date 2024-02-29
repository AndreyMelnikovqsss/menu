# menu/forms.py
from django import forms
from menu.models import MenuItem, Menu  # Используйте полный путь

class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        exclude = []

    def __init__(self, *args, **kwargs):
        super(MenuItemAdminForm, self).__init__(*args, **kwargs)
        # Ограничиваем выбор меню только тем, которые уже созданы
        self.fields['menu'].queryset = Menu.objects.all()
