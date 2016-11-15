# -*- coding : utf-8 -*-
from django.shortcuts import render
from django.views.generic import View,ListView
from .models import Alumni
# Create your views here.
class AlumniListado(View):
	def get(self, request):
		listado = Alumni.objects.inactive()
		return render(request, 'alumni_list.html', {'listado':listado})

