from django.db import models
from django.utils import timezone

STATUS_CHOICES_TYPE = (
	('новый', 'новый'),
	('б/у', 'б/у'),
)

STATUS_CHOICES = (
	('да', 'да'),
	('нет', 'нет'),
)

STATUS_CHOICES_ENG = (
	('K7J', '1,4л/75л.с.(K7J)'),
	('K7M7101', '1,6л/82л.с.(K7M710)'),
	('K7M710', '1,6л/86л.с.(K7M710)'),
	('K7M800', '1,6л/102л.с.(K7M800)'),
	('K7M801', '1,6л/113л.с.')
)

STATUS_CHOICES_KPP = (
	('akpp', 'АКПП'),
	('mkpp', 'МКПП'),
)
class Infodate(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	probeg_tek = models.CharField(max_length=8)
	date_create = models.DateField(auto_now=False)
	probeg_all = models.CharField(max_length=8)
	date_publish = models.DateTimeField(auto_now_add=True)
	conder = models.CharField(max_length=3, choices = STATUS_CHOICES, default='да')
	type_expl = models.CharField(max_length=5, choices = STATUS_CHOICES_TYPE, default='новый')
	type_engine = models.CharField(max_length=20, choices = STATUS_CHOICES_ENG, default='K7J')
	type_kpp = models.CharField(max_length=4, choices = STATUS_CHOICES_KPP, default='mkkp')
	date_oil_last = models.DateField(auto_now=False)
	date_liq_last = models.DateField(auto_now=False)
	date_brake_last = models.DateField(auto_now=False)
	date_to_last = models.DateField(auto_now=False)
	to_make = models.CharField(max_length=3, choices = STATUS_CHOICES, default='да')	
	
def publish(self):
	self.date_publish = timezone.now()
	self.save()

def _str_(self):
	return self.probeg_tek, self.probeg_all, self.conder



# Create your models here.
