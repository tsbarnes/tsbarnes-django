from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Article


class IndexView(generic.ListView):
  model = Article
  template_name = 'blog/index.html'

  def get_queryset(self):
    queryset = Article.objects.filter(published=True)
    return queryset

class DetailView(generic.DetailView):
  model = Article
  template_name = 'blog/detail.html'
