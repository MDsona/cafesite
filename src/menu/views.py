from django.shortcuts import render

# Create your views here.

def home(request):                                      # 1b

    context = {
        'page_title': 'الرئيسية'                       # 1b>1e
    }

    return render(request, 'menu/index.html', context)
