from django.urls import re_path
from users import views

urlpatterns = [
  re_path(r'^job$', views.jobAPI),
  re_path(r'^job/([0-9]+)$', views.jobAPI),
  re_path(r'^department$', views.departmentAPI),
  re_path(r'^department/([0-9]+)$', views.departmentAPI)
]