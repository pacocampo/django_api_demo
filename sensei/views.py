from django.shortcuts import render
from sensei.serializers import SenseiSerializer
from sensei.models import Sensei
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class SenseiList(APIView):
	def get(self, request, format=None):
		seniseis = Sensei.objects.all()
		serializer = SenseiSerializer(seniseis, many=True)
		return Response(serializer.data)