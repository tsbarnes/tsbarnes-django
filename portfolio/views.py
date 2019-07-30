from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import PortfolioItem


class IndexView(generic.ListView):
    model = PortfolioItem
    template_name = 'portfolio/index.html'

class DetailView(generic.DetailView):
    model = PortfolioItem
    template_name = 'portfolio/detail.html'
