from django.db import models 
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
import time


class SingletonModel(models.Model):
  class Meta:
    abstract = True

  def save(self, *args, **kwargs):
    self.__class__.objects.exclude(id=self.id).delete()
    super(SingletonModel, self).save(*args, **kwargs)

  @classmethod
  def load(cls):
    try:
      return cls.objects.get()
    except cls.DoesNotExist:
      return cls()

class Overview(SingletonModel):
    text = models.TextField()
    class Meta:
        verbose_name_plural = "Overview"
    def __unicode__(self):
        return self.text[0:40] + '...'
    
    def __str__(self):
        return self.__unicode__()

class PersonalInfo(SingletonModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    region = models.CharField(max_length=255, help_text="e.g. state such as Massachusetts")
    region_shorthand = models.CharField(max_length=64, help_text="e.g. shorthand (abbr), MA for Massachusetts")
    email = models.EmailField()
    avatar = models.ImageField(blank=True, default='no-img.gif')
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    gitlab = models.URLField(blank=True)
    itchio = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Personal Info"
    
    def full_name(self):
        return " ".join([self.first_name, self.last_name])
    
    def __unicode__(self):
        return self.full_name()
    
    def __str__(self):
        return self.__unicode__()

class Education(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    school_url = models.URLField('School URL')
    start_date = models.DateField()
    completion_date = models.DateField()
    summary = models.TextField()
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-completion_date','-start_date']

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.name, self.edu_date_range()])
    
    def __str__(self):
        return self.__unicode__()


class Job(models.Model):
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    company_url = models.URLField('Company URL')
    description = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField()
    is_current = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    company_image = models.CharField(max_length=250, blank=True, 
        help_text='path to company image, local or otherwise')

    class Meta:
        db_table = 'jobs'
        ordering = ['-completion_date','-start_date']
        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
            return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])
    
    def __str__(self):
        return self.__unicode__()

class Accomplishment(SortableMixin):
    description = models.TextField()
    #job = models.ForeignKey(Job)
    job = models.ForeignKey('Job',on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        db_table = 'accomplishments'
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])
    
    def __str__(self):
        return self.__unicode__()

class Skillset(SortableMixin):
    name = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class Skill(SortableMixin):
    name =  models.CharField(max_length=250)
    skill_url = models.URLField('Skill URL', blank=True)
    skill_level = models.CharField(max_length=20, blank=True)
    skillset = SortableForeignKey('Skillset',on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.skillset.name, '-', self.name])
    
    def __str__(self):
        return self.__unicode__()
