from django.db import models
import uuid

# Create your models here.
class Projects(models.Model):
  ProjectId = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  Team = models.ForeignKey('Team')

class Team(models.Model):
  TeamID = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  
class Meetings(models.Model):
  MeetingID = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  Name = models.CharField(max_length= 200, null=False)
  Date = models.CharField(max_length= 200, null=False)

class MeetingUsersInevited(models.Model):
  User = models.ForeignKey('users.models.Users', null=False)
  Meeting = models.ForeignKey('Meetings', null=False)

class TeamUsers(models.Model):
  User = models.ForeignKey('users.models.Users', null=False)
  Team = models.ForeignKey('Team', null=False)

class Tasks(models.Model):
  Tittle = models.CharField(max_length = 400, null=False)
  SubTittle = models.CharField(max_length = 400, null=True)
  DataStart = models.CharField(max_length = 100, null=False)
  DataEnd = models.CharField(max_length = 100, null=False)
  User = models.ForeignKey('users.models.Users', null=True)
  Project = models.ForeignKey('Projects', null=False)