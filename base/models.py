from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='uploads',null=True)
