from django.conf.urls import url
# from .import views
from .views import calcul, engine, index, input_new
app_name = 'Infodate'

urlpatterns = (
	url(r'^$', index, name='index'),
	url(r'^Calculat', calcul, name='calcul'),
	url(r'^Engine', engine, name='engine'),
	url(r'^Input', input_new, name='input_new'),
)
