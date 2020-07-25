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


