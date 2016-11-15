from django.conf.urls import url, include

urlpatterns = [
	url(r'^sensei/', include('sensei.urls_api')),
]
