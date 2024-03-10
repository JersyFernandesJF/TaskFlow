from rest_framework import serializers
from users.models import Users, Job, Department

class UsersSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Users
    fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Job
    fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Department
    fields =  '__all__'

