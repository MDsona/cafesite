from django.shortcuts import render

from .models import MenuTitle                           # 3a

# Create your views here.

def home(request):                                      # 1b
    menu_titles = MenuTitle.objects.all()               # 3a

    context = {
        'page_title': 'الرئيسية',                      # 1b>1e
        'menu_titles': menu_titles,                     # 3a
    }

    return render(request, 'menu/index.html', context)
