from django.shortcuts import render, redirect       #, 15f

from .forms import NewUserForm, LoginForm, ProfileUpdateForm      # 15b, 16b, 24b
from django.contrib import messages                 # 15f
from django.contrib.auth import authenticate, login, logout            # 16d
from menu.models import ForReser                                       # 23a
from django.contrib.auth.decorators import login_required              # 23c

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
        'page_title': 'تسجيل جديد',
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


def logout_user(request):                                           # 17a
    logout(request)

    return render(request, 'user/logout.html', {
        'page_title': 'تسجيل الخروج',
    })


@login_required(login_url='login_url')                              # 23c
def profile(request):                                               # 23a
    resers = ForReser.objects.filter(author=request.user)
    
    return render(request, 'user/profile.html', {
        'page_title': 'الحساب',
        'resers': resers,
    })


@login_required(login_url='login_url')                                      # 24d
def profile_update(request):                                                # 24b

    # 24d pu_form =ProfileUpdateForm(instance=request.user)

    if request.method == 'POST':                                            # 24d
        pu_form = ProfileUpdateForm(request.POST, instance=request.user)
        if pu_form.is_valid:
            pu_form.save()
            messages.success(request, 'تم تحديث الحساب بنجاح')
            return redirect('profile_url')
    else:
        pu_form = ProfileUpdateForm(instance=request.user)

    return render(request, 'user/profile_update.html', {                    # 24b
        'page_title': 'تحديث الحساب',
        'pu_form': pu_form,
    })


