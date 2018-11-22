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
	('1,4л/75л.с.(K7J)', '1,4л/75л.с.(K7J)'),
	('1,6л/82л.с.(K7M710)', '1,6л/82л.с.(K7M710)'),
	('1,6л/86л.с.(K7M710)', '1,6л/86л.с.(K7M710)'),
	('1,6л/102л.с.(K7M800)', '1,6л/102л.с.(K7M800)'),
	('1,6л/113л.с. (К7М800)', '1,6л/113л.с.(К7М800)')
)

STATUS_CHOICES_KPP = (
	('АКПП', 'АКПП'),
	('МКПП', 'МКПП'),
)
class Infodate(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	probeg_tek = models.CharField(max_length=8, verbose_name="текущий пробег",)
	date_create = models.DateField(auto_now=False, verbose_name="дата приобретения",)
	probeg_all = models.CharField(max_length=8, verbose_name="общий пробег",)
	date_publish = models.DateTimeField(auto_now_add=True, verbose_name="дата публикации",)
	conder = models.CharField(max_length=3, choices = STATUS_CHOICES, default='да', verbose_name="наличие кондиционера",)
	type_expl = models.CharField(max_length=5, choices = STATUS_CHOICES_TYPE, default='новый', verbose_name="тип эксплуатации",)
	type_engine = models.CharField(max_length=20, choices = STATUS_CHOICES_ENG, default='1,4л/75л.с.(K7J)', verbose_name="тип двигателя",)
	type_kpp = models.CharField(max_length=4, choices = STATUS_CHOICES_KPP, default='МКПП', verbose_name="тип КПП",)
	date_oil_last = models.DateField(auto_now=False, verbose_name="дата замены масла(посл.)",)
	date_liq_last = models.DateField(auto_now=False, verbose_name="дата замены ТЖ(посл.)",)
	date_brake_last = models.DateField(auto_now=False, verbose_name="дата замены ОЖ(посл.)",)
	date_to_last = models.DateField(auto_now=False, verbose_name="дата ТО(посл.)",)
	to_make = models.CharField(max_length=3, choices = STATUS_CHOICES, default='да', verbose_name="прохождение ТО",)

	
def publish(self):
	self.date_publish = timezone.now()
	self.save()

def _str_(self):
	return self.probeg_tek, self.probeg_all, self.conder



# Create your models here.
