from rest_framework import serializers
from Users.models import Users, Job, Department

class UsersSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Users
    fields = {'UserID', 'Name', 'Email', 'Password', 'Job'}

class JobSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Job
    fields = {'id', 'Name', 'Department'}

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Department
    fields = {'id', 'Name'}

