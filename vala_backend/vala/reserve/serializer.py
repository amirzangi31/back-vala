from rest_framework import serializers
from .models import reserve,service 
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=service
        fields='__all__'
class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model=reserve
        fields='__all__'