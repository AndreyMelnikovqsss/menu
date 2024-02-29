# menu/templatetags/menu_tags.py
from django import template
from django.utils.html import escape, mark_safe
from ..models import MenuItem, Menu

register = template.Library()


def render_menu_item(request, item):
    active_class = 'active' if request.path == (item.url or item.named_url) else ''
    submenu_items = MenuItem.objects.filter(menu=item.menu, parent=item)
    submenu = [render_menu_item(request, subitem) for subitem in submenu_items]
    return {
        'item': item,
        'is_active': active_class,
        'submenu': submenu,
    }


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu, parent=None).select_related('parent')
    except Menu.DoesNotExist:
        menu_items = []

    menu_data = [render_menu_item(request, item) for item in menu_items]

    def render_menu(menu_data):
        menu_html = ''
        for data in menu_data:
            menu_html += f'<li class="{escape(data["is_active"])}"><a href="{escape(data["item"].url or data["item"].named_url)}">{escape(data["item"].title)}</a>'
            if data['submenu']:
                menu_html += f'<ul>{render_menu(data["submenu"])}</ul>'
            menu_html += '</li>'
        return menu_html

    return mark_safe(render_menu(menu_data))
