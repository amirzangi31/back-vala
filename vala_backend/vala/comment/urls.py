from django.urls import path
from .views import CommentDetail,CommentList,CommentUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',CommentList.as_view()),   
path('GetId/<int:pk>/', CommentDetail.as_view()),
path('GetId/', CommentUser.as_view()),

]
