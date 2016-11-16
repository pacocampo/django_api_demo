from rest_framework import viewsets
from .models import Alumni
from .serializers import AlumniSerializer


class AlumniViewSet(viewsets.ModelViewSet):

	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer