from django.db import models
import uuid

# Create your models here.
class Projects(models.Model):
  ProjectId = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  Team = models.ForeignKey('Team')

class Team(models.Model):
  TeamID = models.IntegerField(primary_key = True)
  Name = models.CharField(max_length= 200, null=False)
  
class Meetings(models.Model):
  MeetingID = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  Date = models.CharField(max_length= 200, null=False)

class MeetingUsersInevited(models.Model):
  User = models.ForeignKey('users.models.Users')
  Meeting = models.ForeignKey('Meetings')