from django.shortcuts import render, redirect       #, 15f

from .forms import NewUserForm                              # 15b
from django.contrib import messages                 # 15f

# Create your views here.

def register(request):                                      # 15b
    # 15f form = NewUserForm()
    if request.method == 'POST':            # 15f
        form = NewUserForm(request.POST)
        if form.is_valid():
            #15g form.save()
            new_user = form.save(commit=False)  # 15g
            # 15g username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1']) # 15g
            new_user.save()
            messages.success(request, f'تم التسجيل بنجاح {new_user}')   # 15g {username}
            return redirect('home_url')

    else:
        form = NewUserForm()

    return render(request, 'user/register.html', {          # 15b
        'form': form,
    })