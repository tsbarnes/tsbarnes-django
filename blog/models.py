from django.db import models
from django.utils import timezone

class Article(models.Model):
  slug = models.SlugField(blank=False)
  title = models.CharField(max_length=255, blank=False)
  subtitle = models.CharField(max_length=255, blank=True)
  header_image = models.ImageField(blank=True)
  short = models.TextField(blank=False)
  text = models.TextField(blank=False)
  date = models.DateField(default=timezone.now)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  published = models.BooleanField(default=False)

  class Meta:
    ordering = ['-date']

  def __unicode__(self):
    return self.title
  
  def __str__(self):
    return self.__unicode__()
