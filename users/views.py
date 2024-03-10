from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.models import Users, Department, Job
from users.serializers import UsersSerializer, DepartmentSerializer, JobSerializer
# Create your views here.

