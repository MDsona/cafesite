from django.urls import path                    # 1c
from . import views


urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # 1c
    path('menu/<int:titleID>/', views.menu_type, name= 'm_type_url'),  # 7b
]