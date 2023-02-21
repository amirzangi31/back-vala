from django.db import models
from user.models import user
from manager.models import manager
from manager.models import manager
# Create your models here.
class food(models.Model):
    name=models.CharField(max_length=50)
    calories=models.IntegerField()
    value=models.IntegerField()
    oprator=models.ForeignKey(manager,on_delete=models.CASCADE)
class program(models.Model):
    Choice =(
        ('Food' , 'Food'),
        ('Sport' ,'Sport'),
    )
    user=models.ForeignKey(user,  on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)
    oprator = models.ForeignKey(manager,on_delete=models.CASCADE)
    types = models.CharField(max_length=20,choices=Choice)
   
class diet(models.Model):
    Choice =(
        ('Breakfast' , 'Breakfast'),
        ('Snack1' ,'Snack1'),
        ('Lunch' ,'Lunch'),
        ('Snack2' ,'Snack2'),
        ('Dinner' ,'Dinner'),

    )
    program = models.ForeignKey(program,  on_delete=models.CASCADE)
    types= models.CharField(max_length=20,choices=Choice)
    food=models.ForeignKey(food,on_delete=models.CASCADE)
    day=models.CharField(max_length=50)
    
class sports(models.Model):
    name=models.CharField(max_length=50)
    time= models.TimeField(auto_now=False, auto_now_add=False)
    day=models.CharField(max_length=50)
    program = models.ForeignKey(program,on_delete=models.CASCADE)
  