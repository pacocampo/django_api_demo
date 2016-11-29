from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from .serializers import AlumniSerializer
from .models import Alumni
from .permissions import ApiUserPermissions

class AlumniList(generics.ListCreateAPIView):
	'''Listado de alumni filtrados por name y activos'''
	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
	filter_fields = ('is_active',)
	search_fields = ('name','mail',)
	

class AlumniDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer

