from django.db import models
from routin.models import routin
from user.models import user
# Create your models here.
class ravand(models.Model):
    routin= models.ForeignKey(routin,on_delete=models.CASCADE)
    image=models.ImageField('home/ravand/' ,null=True)
    created = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    