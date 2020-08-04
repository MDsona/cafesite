from django import forms                                                # 20a
from . models import ForReser


class ForReserForm(forms.ModelForm):                                    # 20a

    # session_duration = forms.FloatField(label='مدة الجلسة')
    # session_date = forms.DateTimeField(label='التوقيت')
    # mobile_number = forms.CharField(label='رقم الجوال')
    
    class Meta:                                                         # 20a
        model = ForReser
        fields = '__all__'

