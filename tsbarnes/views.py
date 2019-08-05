from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from blog.models import Article
from portfolio.models import Project
from resume.models import PersonalInfo, Overview

def index(request):
  return render(request, 'index.html', {
    'articles': Article.objects.all(),
    'projects': Project.objects.all(),
    'personal': PersonalInfo.objects.first(),
    'overview': Overview.objects.first().text,
  })