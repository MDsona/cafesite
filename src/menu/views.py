from django.shortcuts import render

# Create your views here.

def home(request):                                      # 1b

    context = {
        'title': 'home'                                 # 1b
    }

    return render(request, 'menu/index.html', context)
