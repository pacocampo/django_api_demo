from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
	url(r'^sensei/', include('sensei.urls_api')),
	url(r'^alumni/', include('alumni.urls_api')),
	url(r'^auth/', obtain_jwt_token),

	# url(r'^cinta/', include('desescuela.urls_api'))
]
