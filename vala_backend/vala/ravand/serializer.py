from .models import ravand 
from rest_framework import serializers
class RavandSerializer(serializers.ModelSerializer):
    class Meta:
        model=ravand
        fields='__all__'