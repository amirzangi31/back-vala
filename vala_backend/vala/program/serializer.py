from rest_framework import serializers
from user.serializer import UserSerializer
from manager.serializer import ManagerSerializer
from .models import food,diet,sports,program


class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=program
        fields='__all__'
class ProgramGetSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    oprator=ManagerSerializer()
    class Meta:
        model=program
        fields=['user','created','oprator','types']
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=food
        fields='__all__'
class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model=diet
        fields='__all__'
class DietGetSerializer(serializers.ModelSerializer):
    food=FoodSerializer()
    program=ProgramSerializer()
    class Meta:
        model=diet
        fields=['program','day','food','types']
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model=sports
        fields='__all__'
class SportGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=sports
        fields=['name','time','day','program']


