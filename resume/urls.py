from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='resume_home'),
  path('upload', views.upload, name='resume_upload'),
  path('json', views.download, name='resume_json'),
]