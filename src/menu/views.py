from django.shortcuts import render, get_object_or_404  # 7a(404)

from .models import MenuTitle, MenuType                           # 3a

# Create your views here.

def home(request):                                      # 1b, 
    # 8a menu_titles = MenuTitle.objects.all()               # 3a

    context = {
        'page_title': 'الرئيسية',                      # 1b>1e
        # 8a 'menu_titles': menu_titles,                     # 3a
    }

    return render(request, 'menu/index.html', context)


def menu_type(request, titleID):                       # 7a
    title = get_object_or_404(MenuTitle, pk=titleID)
    m_types = MenuType.objects.filter(title_id = titleID)   # 7c
    me_titles = MenuTitle.objects.all()

    context = {
        'page_title': 'القائمة',
        'm_title': title,
        'm_types': m_types,                                 # 7c
        'me_titles': me_titles,
    }

    return render(request, 'menu/menu_type.html', context)


def open_menu(request):                                     # 8a
    menu_titles = MenuTitle.objects.all()

    context = {
        'page_title': 'القائمة',
        'menu_titles': menu_titles,
    }

    return render(request, 'menu/open_menu.html', context)

