from rest_framework import serializers
from .models import Sensei

class SenseiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensei
		fields = ["id", "alias", "mail", "cinta"]
