from django import forms                                                # 20a
from . models import ForReser


class ForReserForm(forms.ModelForm):                                    # 20a

    #session_type = forms.CharField(label='نوع الجلسة', widget=forms.Select(attrs={'class': 'form-control'}))
    #session_date = forms.DateTimeField(label='التوقيت', help_text='YY-MM-DD hh:mm:ss', widget=forms.DateTimeInput(attrs={'class': 'form-control'})) # 26b
    
    class Meta:                                                         # 20a
        model = ForReser
        fields = ['session_type', 'number_of_seats', 'session_duration', 'session_date', 'session_time', 'mobile_number'] # '__all__'

        widgets = {
            'mobile_number': forms.TextInput(attrs={'pattern':'[0-9 ]+'}),
            'session_duration': forms.TextInput(attrs={'pattern':'[1-8 ]+'}),
        }

        # 26b widgets = {                                                     # 25a
        #     'session_type': forms.Select(attrs={'class': 'form-control'}),
        #     'number_of_seats': forms.Select(attrs={'class': 'form-control'}),
        #     'session_duration': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'session_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        #     'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # def clean_mobile_number(self):
    #     mn_cd = self.cleaned_data.get('mobile_number')
    #     if (mn_cd(len) > 10):
    #         raise forms.ValidationError('رقم غير صحيح')
    #     return mn_cd

