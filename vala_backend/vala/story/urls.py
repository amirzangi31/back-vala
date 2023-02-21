from django.urls import path
from .views import StoryDetail,StoryList,StoryUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',StoryList.as_view()),   
path('GetId/<int:pk>/', StoryDetail.as_view()),
path('GetId/', StoryUser.as_view()),

]
