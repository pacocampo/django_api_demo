from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views_api import AlumniList,AlumniDetail
from .views_apiset import AlumniViewSet

# router = DefaultRouter()

# router.register(r'', AlumniViewSet)

urlpatterns = [
	# url(r'^',include(router.urls) ),
	url(r'^listado/', AlumniList.as_view())

]

