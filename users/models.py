from django.db import models
import uuid

# Create your models here.
class Users(models.Model):
  UserID = models.UUIDField(default=uuid.uuid4, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  Email = models.EmailField(unique=True, null=False)
  Password = models.CharField(null=False, max_length= 300)
  Job = models.ForeignKey('Job', on_delete=models.CASCADE)

class Job(models.Model):
  JobID = models.IntegerField(primary_key=True)
  Name = models.CharField(unique = True, null=False, max_length= 200)
  Department = models.ForeignKey('Department', on_delete=models.CASCADE)

class Department(models.Model):
  
  DepartmentId = models.IntegerField(primary_key = True)
  Name = models.CharField(unique=True, null=False, max_length= 200)
  