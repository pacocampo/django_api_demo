from django.conf.urls import url
from .views import AlumniListado

urlpatterns = [
	url(r'^listado/', AlumniListado.as_view(), name="alumni_listado")
]