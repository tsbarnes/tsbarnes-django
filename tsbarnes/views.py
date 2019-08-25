from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from blog.models import Article
from portfolio.models import Project
from resume.models import Basics, Profile

def index(request):
  return render(request, 'index.html', {
    'articles': Article.objects.filter(published=True)[0:3],
    'projects': Project.objects.filter(published=True)[0:5],
    'basics': Basics.objects.first(),
    'profiles': Profile.objects.all()
  })