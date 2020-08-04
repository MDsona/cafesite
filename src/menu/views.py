from django.shortcuts import render, get_object_or_404  # 7a(404)

from .models import MenuTitle, MenuType, MenuContent, MapBox, ForReser   # 3a, , , 12c, 21a
from .forms import ForReserForm                                     # 20b
from django.views.generic import CreateView                              # 21a
from django.contrib.auth.mixins import LoginRequiredMixin  #21e

# Create your views here.

def home(request):                                      # 1b, 
    # 8a menu_titles = MenuTitle.objects.all()               # 3a

    context = {
        'page_title': 'الرئيسية',                      # 1b>1e
        # 8a 'menu_titles': menu_titles,                     # 3a
    }

    return render(request, 'menu/index.html', context)


def menu_type(request, titleID):                       # 7a 
    # title = get_object_or_404(MenuTitle, pk=titleID)
    # >< m_types = MenuType.objects.filter(title_id = titleID)   # 7c
    me_titles = MenuTitle.objects.all()

    types = get_object_or_404(MenuTitle, pk=titleID)            # 7d

    context = {
        'page_title': 'القائمة',
        # 'm_title': title,
        # >< 'm_types': m_types,                                 # 7c
        'me_titles': me_titles,

        'types': types                                          # 7d
    }

    return render(request, 'menu/menu_type.html', context)


def open_menu(request):                                     # 8a
    menu_titles = MenuTitle.objects.all()

    context = {
        'page_title': 'القائمة',
        'menu_titles': menu_titles,
    }

    return render(request, 'menu/open_menu.html', context)


def menu_content(request, titleID, typeID):                          # 10a
    # 10c content_m = MenuContent.objects.all()
    contents = get_object_or_404(MenuType, title_id=titleID, pk= typeID)  # or (, title__pk=,) 10c
    titles = MenuTitle.objects.all()

    conTypes = MenuType.objects.filter(title_id=titleID)            # 10d

    context = {
        'page_title': 'محتوى القائمة',
        # 10c 'content_m': content_m,
        'contents': contents,                           # 10c
        'titles': titles,

        'conTypes': conTypes                                        # 10d
    }

    return render(request, 'menu/menu_content.html', context)


def open_map(request):                                              # 11a

    # d map_url = MapBox.objects.all()                              # 12c
    map_url = MapBox.objects.filter(mapActive=True)                 # 13d

    context = {
        'page_title': 'العنوان',                                     # a11 
        'map_urls': map_url,                                          # 12c

    }

    return render(request, 'menu/open_map.html', context)


#  # 20c - function based views

# def for_reservations(request):                                          # 14a    
#     form = ForReserForm()                                               # 20b    
#     context = {
#         'page_title': 'حجز جلسة',
#         'form': form,
#     }
#     return render(request, 'menu/for_reser.html', context)                       # 14a



class ForReserCreatView(LoginRequiredMixin, CreateView):       # (21e, 21a)
    model = ForReser
    # 21d fields = ['session_duration', 'session_date']
    template_name = 'menu/for_reser.html'
    form_class = ForReserForm   # 21d

    def form_valid(self, form):                                         # 21c
        form.instance.author = self.request.user
        return super().form_valid(form)

