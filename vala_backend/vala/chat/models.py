from django.db import models
from user.models import user 
from manager.models import manager
# Create your models here.
class chat(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    
class chatReply(models.Model):
    oprators = models.ForeignKey(manager,on_delete=models.CASCADE)
    chat=models.ForeignKey(chat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()