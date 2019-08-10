from django.db import models
from django.utils import timezone
from adminsortable.models import SortableMixin
from resume.models import Job

class Project(SortableMixin):
  slug = models.SlugField(blank=False)
  title = models.CharField(max_length=255, blank=False)
  subtitle = models.CharField(max_length=255, blank=True)
  header_image = models.ImageField(blank=True, default='no-img.gif')
  short = models.TextField(blank=False)
  text = models.TextField(blank=False)
  technologies = models.CharField(max_length=512, blank=True)
  date = models.DateField(default=timezone.now, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  published = models.BooleanField(default=False)
  job = models.ForeignKey(Job, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

  class Meta:
      ordering = ['order']

  def __unicode__(self):
    return self.title
  
  def __str__(self):
    return self.__unicode__()
