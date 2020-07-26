from django.urls import path                                    # 15c
from . import views


urlpatterns = [
    path('register/', views.register, name= 'register_url'),    # 15c
    path('login/', views.login_user, name= 'login_url'),        # 16c
    path('logout/', views.logout_user, name= 'logout_url'),     # 17b
]

