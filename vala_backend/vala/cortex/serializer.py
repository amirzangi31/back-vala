from .models import cortex,oprator_Laser 
from rest_framework import serializers
from user.serializer import UserSerializer
class CortexSerializer(serializers.ModelSerializer):
    class Meta:
        model=cortex
        fields='__all__'
class GetCortexSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=cortex
        fields=['district','numbermeet','descriptions','oprator_Las','created','user']
class Oprator_laserSerializer(serializers.ModelSerializer):
    class Meta:
        model=oprator_Laser
        fields='__all__'