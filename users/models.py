from django.db import models
import uuid
import bcrypt

# Create your models here.
class Users(models.Model):
  userID = models.UUIDField(default=uuid.uuid4, unique=True, editable = False, primary_key= True, null=False)
  name = models.CharField(max_length= 200, null=False)
  email = models.EmailField(unique=True, null=False, blank=False)
  password = models.CharField(null=False, max_length= 300, blank=False)
  job = models.ForeignKey('Job', on_delete=models.CASCADE, null=False)

  def __str__(self):
    return self.Name
  
  def hash_password(self, password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
  
  def verify_password(self,input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

class Job(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(unique = True, null=False, max_length= 200)
  nepartment = models.ForeignKey('Department', on_delete=models.CASCADE, null=False)

class Department(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(unique=True, null=False, max_length= 30, blank=True)
  