from django.forms import ModelForm
from .models import Infodate

class InfodateForm(ModelForm):

    class Meta:
        model = Infodate
        fields = ('date_create', 'type_engine', 'type_kpp', 'probeg_tek', 'probeg_all', 'type_expl', 'date_oil_last', 'date_liq_last', 'date_brake_last', 'to_make', 'date_to_last', 'conder',)
