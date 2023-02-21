from django.db import models
from user.models import user
from post.models import post
# Create your models here.
class comment(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    text=models.TextField()
    post=models.ForeignKey(post, on_delete=models.CASCADE)
    accepted=models.BooleanField()