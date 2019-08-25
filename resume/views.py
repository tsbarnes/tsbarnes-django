from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .models import Overview, PersonalInfo, SocialAccount, Education, Job, Accomplishment, Skillset, Skill

def index(request):
  personal_info = PersonalInfo.objects.first()
  overview = Overview.objects.first()
  social_accounts = SocialAccount.objects.all()
  education = Education.objects.all()
  job_list = Job.objects.filter(is_public=True)
  skill_sets = Skillset.objects.all()

  return render(request, 'resume/resume.html', {
    'personal_info': personal_info,
    'overview' : overview,
    'social_accounts' : social_accounts,
    'job_list' : job_list,
    'education' : education,
    'skill_sets' : skill_sets,
  })

# TODO: add ability to upload a jsonresume
@login_required
def upload(request):
  pass

# TODO: add ability to download resume as json
def json(request):
  pass