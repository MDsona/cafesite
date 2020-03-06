from django.contrib import admin

from .models import MenuTitle, MenuType               # 2b, 6b

# Register your models here.

admin.site.register(MenuTitle)              # 2b
admin.site.register(MenuType)              # 6b
