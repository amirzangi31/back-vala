from .models import chat,chatReply
from rest_framework import serializers
from user.serializer import UserSerializer
from manager.serializer import ManagerSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=chat
        fields='__all__'
class GetchatSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=chat
        fields=['pk','created','description','user']
       
        
 
class ChatReplySerializer(serializers.ModelSerializer):
    class Meta:
        model=chatReply
        fields='__all__'
        
class GetchatReplySerializer(serializers.ModelSerializer):
    oprators=ManagerSerializer()
    chat = ChatSerializer()
    class Meta:
        model=chatReply
        fields=['pk','created','description','chat','oprators']   

        
        


 