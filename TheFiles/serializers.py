from rest_framework import serializers
from .models import Federation

class FederationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Federation
		fields ='__all__'