from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    model = Project
    template_name = 'portfolio/index.html'

class DetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/detail.html'
