from django.db import models
import uuid


# Create your models here.
class Projects(models.Model):
  projectId = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  name = models.CharField(max_length= 200, null=False)
  team = models.ForeignKey('Team', models.SET_NULL, blank= True, null=True)

class Team(models.Model):
  teamID = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  name = models.CharField(max_length= 200, null=False)
  
class Meetings(models.Model):
  meetingID = models.UUIDField(default=uuid.uuid1, unique=True, editable = False, primary_key= True, null=False)
  name = models.CharField(max_length= 200, null=False)
  date = models.CharField(max_length= 200, null=False)

class MeetingUsersInevited(models.Model):
  user = models.ForeignKey('users.Users', null=False, on_delete=models.CASCADE)
  meeting = models.ForeignKey('Meetings', null=False, on_delete=models.CASCADE)

class TeamUsers(models.Model):
  user = models.ForeignKey('users.Users', null=False, on_delete=models.CASCADE)
  team = models.ForeignKey('Team', on_delete=models.CASCADE)

class Tasks(models.Model):
  tittle = models.CharField(max_length = 400, null=False)
  subTittle = models.CharField(max_length = 400, null=True)
  dataStart = models.CharField(max_length = 100, null=False)
  dataEnd = models.CharField(max_length = 100, null=False)
  user = models.ForeignKey('users.Users', models.SET_NULL, blank= True, null= True)
  project = models.ForeignKey('Projects', null=False, on_delete=models.CASCADE)