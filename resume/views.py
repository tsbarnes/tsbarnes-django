from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import json
from collections import namedtuple

from .models import Basics, Profile, Education, Work, Volunteer, Skillset, Skill
from .forms import JsonForm

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
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = JsonForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      rawdata = form.cleaned_data["json"]
      data = json.loads(rawdata, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

      basics, created = Basics.objects.get_or_create()

      basics.label = data.basics.label
      basics.email = data.basics.email
      basics.phone = data.basics.phone
      basics.summary = data.basics.summary

      basics.save()

      # redirect to a new URL:
      return HttpResponseRedirect('/resume/')

  # if a GET (or any other method) we'll create a blank form
  else:
    form = JsonForm()

  return render(request, 'resume/upload.html', {'form': form})

# TODO: add ability to download resume as json
def download(request):
  resume = {
    "basics": {
    }
  }

  basics = Basics.objects.first()
  resume["basics"]["name"] = basics.name()
  resume["basics"]["label"] = basics.label
  resume["basics"]["email"] = basics.email
  resume["basics"]["phone"] = basics.phone
  resume["basics"]["website"] = RequestSite(request).domain
  resume["basics"]["summary"] = basics.summary
  resume["basics"]["location"] = {
    "city": basics.location.city,
    "region": basics.location.region,
  }
  resume["basics"]["profiles"] = []
  for profile in Profile.objects.all():
    resume["basics"]["profiles"].append({
      "network": profile.network,
      "username": profile.username,
      "url": profile.url,
    })
  
  resume["work"] = []
  for work in Work.objects.all():
    obj = {
      "company": work.company,
      "position": work.position,
      "website": work.website,
      "startDate": work.start_date,
      "endDate": work.end_date,
      "summary": work.summary,
      "highlights": [],
    }
    for highlight in work.highlight_set.all():
      obj["highlights"].append(highlight.description)
    resume["work"].append(obj)

  return JsonResponse(resume)