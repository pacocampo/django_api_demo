from rest_framework import serializers
from .models import Sensei
from desescuela.serializers import CintaSerializer

class SenseiSerializer(serializers.ModelSerializer):

	cinta = CintaSerializer(many = True, read_only= True)

	class Meta:
		model = Sensei
		fields = ["id", "alias", "mail", "cinta"]
