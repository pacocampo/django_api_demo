from rest_framework import serializers
from .models import Cinta
from alumni.serializers import AlumniSerializer

class CintaSerializer(serializers.ModelSerializer):

	cinta_alumni = AlumniSerializer(many=True, read_only=True)

	class Meta:
		model = Cinta
		fields = ['id', 'color', 'is_active', 'cinta_alumni']