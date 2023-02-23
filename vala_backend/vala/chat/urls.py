from django.urls import path
from .views import ChatDetail,ChatList,ChatUser,ChatReplyDetail,ChatReplyList,ChatReplyChat
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',ChatList.as_view()),   
path('GetId/<int:pk>/', ChatDetail.as_view()),
path('GetId/', ChatUser.as_view()),

path('reply/all/',ChatReplyList.as_view()),   
path('reply/GetId/<int:pk>/', ChatReplyDetail.as_view()),
path('GetId/', ChatReplyChat.as_view()),

]
