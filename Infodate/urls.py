from django.conf.urls import url
# from .import views
from .views import calcul, engine, index, input_new
app_name = 'Infodate'

urlpatterns = (
	url(r'^$', index, name='index'),
	url(r'^/InfodateCalcul/', calcul, name='calcul'),
	url(r'^/InfodateEngine/', engine, name='engine'),
    url(r'^/InfodateInput/', input_new, name='input_new'),
)
