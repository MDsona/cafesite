from django import forms                                    # 15a
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):                         # 15a
    username = forms.CharField(label='إسم المستخدم', max_length=30)
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:                                             # 15a
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def clean_password2(self):          # 15e
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']
    
    def clean_username(self):           # 15e
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم بهذا الاسم')
        return cd['username']


class LoginForm(forms.ModelForm):                                           # 16a
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileUpdateForm(forms.ModelForm):                                   # 24a

    username = forms.CharField(label='اسم المستخدم')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


