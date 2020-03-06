from django.shortcuts import render

# 4a from .models import MenuTitle                           # 3a

# Create your views here.

def home(request):                                      # 1b
    # 4a menu_titles = MenuTitle.objects.all()               # 3a

    context = {
        'page_title': 'الرئيسية',                      # 1b>1e
        # 4a 'menu_titles': menu_titles,                     # 3a
    }

    return render(request, 'menu/index.html', context)
