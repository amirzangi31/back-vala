from django.db import models

# Create your models here.
class story(models.Model):
    title = models.CharField(max_length=50)
    file=models.FileField(upload_to='home/story/')
    created=models.DateTimeField( auto_now_add=True)