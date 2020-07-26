from django.shortcuts import render, redirect       #, 15f

from .forms import NewUserForm, LoginForm                              # 15b, 16b
from django.contrib import messages                 # 15f
from django.contrib.auth import authenticate, login, logout            # 16d

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


def login_user(request):                                            # 16b
    if request.method == 'POST':                                    # 16d
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home_url')
        else:
            messages.warning(request, 'خطأ في اسم المستخدم أو كلمة المرور')
        
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {                     # 16b
        'page_title': 'تسجيل الدخول',
        'form': form,
    })


