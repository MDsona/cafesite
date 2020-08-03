from django.contrib import admin

from .models import MenuTitle, MenuType, MenuContent, MapBox, SessionType, NumberOFseats, ForReser   # 2b, 6b, 9b, 12b, 18a,b, 19b

# Register your models here.

admin.site.register(MenuTitle)              # 2b
admin.site.register(MenuType)               # 6b
admin.site.register(MenuContent)            # 9b
admin.site.register(MapBox)                 # 12b 
admin.site.register(SessionType)            # 18a
admin.site.register(NumberOFseats)          # 18b
admin.site.register(ForReser)               # 19b


