from django.contrib import admin
from .models import Infodate

class InfoAdmin(admin.ModelAdmin):
	list_display = ('date_publish', 'date_create', 'type_engine', 'type_kpp', 'probeg_tek', 'probeg_all',
	'type_expl', 'date_oil_last', 'date_liq_last', 'date_brake_last', 'date_to_last', 'to_make', 'conder', 'author')
	ordering = ['date_publish']
#	list_filter = ('date_create')
#	search_fields = ('author')

admin.site.register(Infodate, InfoAdmin)
# Register your models here.
