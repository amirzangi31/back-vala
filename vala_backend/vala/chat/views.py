from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import ChatSerializer,GetchatSerializer,ChatReplySerializer,GetchatReplySerializer

from .models import chat,chatReply
# Create your views here.

class ChatList(APIView):
    def get(self,request):
        querysert = chat.objects.all()
        serial = GetchatSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChatDetail(APIView):
    def get_object(self,pk):
        try:   
            return chat.objects.get(pk=pk)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = GetchatSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk2)
        serializer = ChatSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChatUser(APIView):

    def get_object(self,user):
        try:   
            return chat.objects.filter(user=user)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = GetchatSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
    
    
class ChatReplyList(APIView):
    def get(self,request):
        querysert = chatReply.objects.all()
        serial = GetchatReplySerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = ChatReplySerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChatReplyDetail(APIView):
    def get_object(self,pk):
        try:   
            return chatReply.objects.get(pk=pk)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = GetchatReplySerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk2)
        serializer = ChatReplySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChatReplyChat(APIView):

    def get_object(self,user):
        try:   
            return chatReply.objects.filter(chat=user)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = GetchatSerializer(queryset,many=True)
        return Response(serializer.data)
    