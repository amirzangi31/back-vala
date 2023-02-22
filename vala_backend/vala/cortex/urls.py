from django.urls import path
from .views import CortexList,CortexDetail,CortexUser,oprator_laserList,oprator_laserDetail,oprator_laserUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',CortexList.as_view()),   
path('GetId/<int:pk>/', CortexDetail.as_view()),
path('GetId/', CortexUser.as_view()),

path('op/all/',oprator_laserList.as_view()),   
path('op/GetId/<int:pk>/', oprator_laserDetail.as_view()),
path('op/GetId/', oprator_laserUser.as_view()),
]
