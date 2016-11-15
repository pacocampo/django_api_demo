from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SenseiSerializer
from .models import Sensei

class SenseiListadoView(APIView):
	'''Devuelve listado de Senseis'''
	def get(self, request, format=None):
		listado = Sensei.objects.all()
		serializer = SenseiSerializer(listado, many=True)
		return Response(serializer.data)


