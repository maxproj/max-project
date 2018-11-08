from django import forms
from .models import Infodate

class InfodateForm(forms.ModelForm):

    class Meta:
        model = Infodate
        fields = ('date_create', 'type_engine', 'type_kpp', 'probeg_tek', 'probeg_all', 'type_expl', 'date_oil_last', 'date_liq_last', 'date_brake_last', 'date_to_last', 'to_make', 'conder',)

