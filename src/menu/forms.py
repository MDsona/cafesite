from django import forms                                                # 20a
from . models import ForReser


class ForReserForm(forms.ModelForm):                                    # 20a

    #session_date = forms.DateTimeField(label='التوقيت')
    
    class Meta:                                                         # 20a
        model = ForReser
        fields = fields = ['session_type', 'number_of_seats', 'session_duration', 'session_date', 'mobile_number'] # '__all__'

