from django.conf.urls import url, include

urlpatterns = [
	url(r'^sensei/', include('sensei.urls_api')),
	url(r'^alumni/', include('alumni.urls_api')),
	# url(r'^cinta/', include('desescuela.urls_api'))
]
