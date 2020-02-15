from django.urls import path                    # 1c
from . import views


urlpatterns = [                                        
    path('', views.home, name= 'home_url'),            # 1c
]