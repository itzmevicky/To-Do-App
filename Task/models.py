from django.db import models

from django.contrib.auth.models import User
import datetime
# Create your models here.

class TodoTask(models.Model):
   timeStamp = models.DateTimeField(auto_now_add=True)
   createdBy = models.ForeignKey(User,on_delete=models.CASCADE)
   status = (
      ('O', 'Open'),
      ('W', 'Working'),
      ('D' ,'Done'),
      ('OD', 'Overdue')
   )
   Title = models.CharField(max_length=100) 
   Description = models.TextField(max_length=1000)
   DueDate = models.DateField(blank=True,null=True)
   Tags = models.CharField(blank=True,null=True,max_length=500)
   Status = models.CharField(choices=status,max_length=2)


   def __str__(self) -> str:
      return self.Title
   
   