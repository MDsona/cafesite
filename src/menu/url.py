from django.urls import path                    # 1c
from . import views


urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # 1c
    path('menu/<int:titleID>/', views.menu_type, name= 'm_type_url'),  # 7b
    path('menu', views.open_menu, name= 'open_menu_url'),              # 8b
    path('menu/<int:titleID>/content/<int:typeID>/', views.menu_content, name= 'm_content_url'), # 10b
]