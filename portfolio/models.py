from django.db import models
from django.utils import timezone

class Project(models.Model):
  slug = models.SlugField(blank=False)
  title = models.CharField(max_length=255, blank=False)
  subtitle = models.CharField(max_length=255, blank=True)
  header_image = models.ImageField(blank=True, default='no-img.gif')
  short = models.TextField(blank=False)
  text = models.TextField(blank=False)
  technologies = models.CharField(max_length=512, blank=True)
  date = models.DateField(default=timezone.now)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  published = models.BooleanField(default=False)

  def __unicode__(self):
    return self.title