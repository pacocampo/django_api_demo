from django.conf.urls import url
from .views_api import SenseiListadoView, SenseiDetalleView

urlpatterns = [
	url(r'^listado/', SenseiListadoView.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', SenseiDetalleView.as_view()),
]