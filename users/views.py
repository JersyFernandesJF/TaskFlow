from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import bcrypt

from users.models import Users, Department, Job
from users.serializers import UsersSerializer, DepartmentSerializer, JobSerializer
# Create your views here.

def hash_password(password):
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed_password

@csrf_exempt
def authAPI(request, id=0):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = hash_password(request.POST.get('password'))
    

    user = Users.objects.get(email = email)

@csrf_exempt 
def jobAPI(request, id=0):
  if request.method == 'POST':
    job_data = JSONParser().parse(request)
    job_serializer = JobSerializer(data=job_data)
    if job_serializer.is_valid():
      job_serializer.save()
      return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to add")

@csrf_exempt 
def departmentAPI(request):
  if request.method == 'POST':
    department_data = JSONParser().parse(request)
    department_serializer = DepartmentSerializer(data=department_data)
    if department_serializer.is_valid():
      department_serializer.save()
      return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to add", safe=False)