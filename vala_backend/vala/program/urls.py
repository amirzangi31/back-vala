from django.urls import path
from .views import FoodDetail,FoodList,DietDetail,DietList,SportDetail,SportList,ProgramDetail,ProgramList,ProgramUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('food/all/',FoodList.as_view()),   
path('food/GetId/<int:pk>/', FoodDetail.as_view()),

path('diet/all/',DietList.as_view()),   
path('diet/GetId/<int:pk>/', DietDetail.as_view()),


path('sport/all/',SportList.as_view()),   
path('sport/GetId/<int:pk>/', SportDetail.as_view()),

path('program/all/',ProgramList.as_view()),   
path('program/GetId/<int:pk>/', ProgramDetail.as_view()),
path('program/GetId/', ProgramUser.as_view()),
]
