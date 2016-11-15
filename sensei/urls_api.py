from django.conf.urls import url
from .views_api import SenseiListadoView

urlpatterns = [
	url(r'^listado/', SenseiListadoView.as_view()),
]