from rest_framework import generics
from rest_framework.response import Response
from .serializers import AlumniSerializer
from .models import Alumni



class AlumniList(generics.ListCreateAPIView):

	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer

class AlumniDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer