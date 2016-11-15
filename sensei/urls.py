from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', index, name="sites-index"),
    url(r'^listado/$',Register.as_view(), name="sensei-listado"),  
]