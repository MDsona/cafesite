from django.urls import path                    # 1c
from . import views
from django.conf.urls.static import static                           # 13c
from django.conf import settings


urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # 1c
    path('menu', views.open_menu, name= 'open_menu_url'),              # 8b
    path('menu/<int:titleID>/', views.menu_type, name= 'm_type_url'),  # 7b
    path('menu/<int:titleID>/content/<int:typeID>/', views.menu_content, name= 'm_content_url'), # 10b
    path('map', views.open_map, name= 'open_map_url'),              # 11b

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # 13c
