from rest_framework import serializers
from .models import Alumni


class AlumniSerializer(serializers.ModelSerializer):

	class Meta:
		model = Alumni
		exclude = ["alias"]