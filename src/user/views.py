from django.shortcuts import render

from .forms import NewUserForm                              # 15b

# Create your views here.

def register(request):                                      # 15b
    form = NewUserForm()

    return render(request, 'user/register.html', {          # 15b
        'form': form,
    })