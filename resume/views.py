from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Basics, Profile, Education, Work, Volunteer, Skillset, Skill

def index(request):
  site_name = RequestSite(request).domain
  basics = Basics.objects.first()
  profiles = Profile.objects.all()
  education = Education.objects.all()
  work = Work.objects.all()
  volunteer_work = Volunteer.objects.all()
  skill_sets = Skillset.objects.all()

  return render(request, 'resume/resume.html', {
    'site_name': site_name,
    'basics': basics,
    'profiles' : profiles,
    'work' : work,
    'volunteer_work': volunteer_work,
    'education' : education,
    'skill_sets' : skill_sets,
  })

# TODO: add ability to upload a jsonresume
@login_required
def upload(request):
  pass

# TODO: add ability to download resume as json
def json(request):
  resume = {
    "basics": {
    }
  }

  personal_info = PersonalInfo.objects.first()
  resume["basics"]["name"] = personal_info.full_name()
  resume["basics"]["email"] = personal_info.email
  resume["basics"]["website"] = RequestSite(request).domain
  resume["basics"]["summary"] = Overview.objects.first().text
  resume["basics"]["location"] = {
    "city": personal_info.locality,
    "region": personal_info.region,
  }

  return JsonResponse(resume)