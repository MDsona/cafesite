from django.urls import path                                    # 15c
from . import views


urlpatterns = [
    path('register/', views.register, name= 'register_url'),    # 15c
]

