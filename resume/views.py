from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext

from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill

def index(request):
  site_name = RequestSite(request).domain
  personal_info = PersonalInfo.objects.first()
  overview = Overview.objects.first()
  education = Education.objects.all()
  job_list = Job.objects.filter(is_public=True)
  skill_sets = Skillset.objects.all()

  return render(request, 'resume/resume.html', {
    'site_name': site_name,
    'personal_info': personal_info,
    'overview' : overview,
    'job_list' : job_list,
    'education' : education,
    'skill_sets' : skill_sets,
  })

# TODO: add ability to upload a jsonresume
def upload(request):
  pass

# TODO: add ability to download resume as json
def json(request):
  pass