import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import SenseiSerializer
from django.shortcuts import get_object_or_404
from .models import Sensei
from rest_framework import status

class SenseiSearch(generics.ListCreateAPIView):
	serializer_class = SenseiSerializer

	def get_queryset(self):
		print("queryset")
		name = self.kwargs["alias"]
		return Sensei.objects.filter(alias=name)

class SenseiListadoView(APIView):
	'''Devuelve listado de Senseis'''
	def get(self, request, format=None):
		listado = Sensei.objects.all()
		serializer = SenseiSerializer(listado, many=True)
		return Response(serializer.data)

	def post(self,request,format=None):

		sensei = SenseiSerializer(data=request.data)

		if sensei.is_valid():

			sensei.save()

			return Response(sensei.data,status=status.HTTP_201_CREATED)
		return Response(sensei.errors, status=status.HTTP_400_BAD_REQUEST)


class SenseiDetalleView(APIView):

	def get(self,request,pk,format=None):

		sensei = get_object_or_404(Sensei,pk=pk)

		serializer = SenseiSerializer(sensei)

		return Response(serializer.data)

	def put(self,request,pk,format=None):

		sensei = get_object_or_404(Sensei,pk=pk)

		serializer = SenseiSerializer(sensei,request.data)

		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



	def delete(self,request,pk,format=None):

		sensei = get_object_or_404(Sensei,pk=pk)

		sensei.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)























