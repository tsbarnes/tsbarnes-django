from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import json
from collections import namedtuple

from .models import Basics, Profile, Education, Course, Work, Volunteer, Skill, SkillKeyword, Location, Highlight
from .forms import JsonForm

def index(request):
  site_name = RequestSite(request).domain
  basics = Basics.objects.first()
  profiles = Profile.objects.all()
  education = Education.objects.all()
  work = Work.objects.all()
  volunteer_work = Volunteer.objects.all()
  skill_sets = Skill.objects.all()

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
      if created:
        basics.location = Location.objects.create()
      try:
        basics.location.address = data.basics.address
      except:
        pass
      try:
        basics.location.postal_code = data.basics.postalCode
      except:
        pass
      try:
        basics.location.city = data.basics.city
      except:
        pass
      try:
        basics.location.country_code = data.basics.countryCode
      except:
        pass
      try:
        basics.location.region = data.basics.region
      except:
        pass

      basics.location.save()
      basics.save()

      for profile in Profile.objects.all():
        profile.delete()
      c = 0
      for profile in data.basics.profiles:
        c = c + 1
        p = Profile.objects.create(
          network=profile.network,
          username=profile.username,
          url=profile.url,
          icon_name=profile.network.lower(),
          order=c
        )
        p.save()
      
      for work in Work.objects.all():
        work.delete()
      for work in data.work:
        try:
          endDate = work.endDate
          website = work.website
        except:
          endDate = None
          website = None
        w = Work.objects.create(
          summary=work.summary,
          start_date=work.startDate,
          end_date=endDate,
          website=website,
          position=work.position,
          company=work.company
        )
        w.save()
        c = 0
        for highlight in work.highlights:
          c = c + 1
          h = Highlight.objects.create(
            description=highlight,
            job=w,
            order=c
          )
          h.save()

      for work in Volunteer.objects.all():
        work.delete()
      for work in data.volunteer:
        try:
          endDate = work.endDate
          website = work.website
        except:
          endDate = None
          website = None
        w = Work.objects.create(
          summary=work.summary,
          start_date=work.startDate,
          end_date=endDate,
          website=website,
          position=work.position,
          organization=work.organization
        )
        w.save()
        c = 0
        for highlight in work.highlights:
          c = c + 1
          h = VolunteerHighlight.objects.create(
            description=highlight,
            job=w,
            order=c
          )
          h.save()

      for skill in Skill.objects.all():
        skill.delete()
      for skill_data in data.skills:
        skill = Skill.objects.create(
          name=skill_data.name
        )
        try:
          skill.level = skill_data.level
        except:
          pass
        try:
          skill.url = skill_data.url
        except:
          pass
        skill.save()
        for keyword_data in skill_data.keywords:
          keyword = SkillKeyword.objects.create(
            name=keyword_data,
            skill=skill
          )
          keyword.save()

      for edu in Education.objects.all():
        edu.delete()
      for edu_data in data.education:
        edu = Education.objects.create(
          institution=edu_data.institution,
          area=edu_data.area,
          start_date=edu_data.startDate
        )
        try:
          edu.gpa = edu_data.gpa
        except:
          pass
        try:
          edu.end_date = edu_data.endDate
        except:
          pass
        try:
          edu.study_type = edu_data.studyType
        except:
          pass
        edu.save()
        for course_data in edu_data.courses:
          course = Course.objects.create(
            name=course_data,
            education=edu
          )
          course.save()


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
    "address": basics.location.address,
    "postalCode": basics.location.postal_code,
    "city": basics.location.city,
    "countryCode": basics.location.country_code,
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