from django.contrib import admin

from .models import MenuTitle, MenuType, MenuContent, MapBox               # 2b, 6b, 9b, 12b

# Register your models here.

admin.site.register(MenuTitle)              # 2b
admin.site.register(MenuType)              # 6b
admin.site.register(MenuContent)            # 9b
admin.site.register(MapBox)                 # 12b 


