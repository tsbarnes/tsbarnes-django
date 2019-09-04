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

class Basics(SingletonModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    label = models.CharField(max_length=250, blank=True)
    picture = models.ImageField(blank=True, default='no-img.gif')
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Basics"

    def name(self):
        return " ".join([self.first_name, self.last_name])
    
    def website(self):
        return ''.join(["https://", RequestSite(request).domain])
    
    def __unicode__(self):
        return self.name()
    
    def __str__(self):
        return self.__unicode__()

class Location(models.Model):
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    country_code = models.CharField(max_length=3, default="US")
    region = models.CharField(max_length=255, help_text="e.g. state such as Massachusetts")
    region_shorthand = models.CharField(max_length=64, help_text="e.g. shorthand (abbr), MA for Massachusetts")

class Profile(SortableMixin):
    network = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=30, default="mail")
    username = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        if self.username:
            return ''.join([self.username, ' on ', self.network])
        return self.network
    
    def __str__(self):
        return self.__unicode__()

class Education(models.Model):
    institution = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    school_url = models.URLField('School URL', blank=True, null=True)
    study_type = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    gpa = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-end_date','-start_date']

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if not self.end_date:
            return None
        else:
            return self.end_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if not self.end_date:
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.institution, self.edu_date_range()])
    
    def __str__(self):
        return self.__unicode__()

class Course(SortableMixin):
    name = models.CharField(max_length=250)
    education = SortableForeignKey('Education', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])
    
    def __str__(self):
        return self.__unicode__()

class Work(models.Model):
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    website = models.URLField('Company URL', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.TextField()

    class Meta:
        verbose_name_plural = "Work"
        ordering = ['-end_date','-start_date']
        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if not self.end_date:
            return None
        else:
            return self.end_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
            return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if not self.end_date:
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])
    
    def __str__(self):
        return self.__unicode__()

class Volunteer(models.Model):
    organization = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    website = models.URLField('Company URL')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.TextField()

    class Meta:
        verbose_name = "Volunteer Work"
        verbose_name_plural = "Volunteer Work"
        ordering = ['-end_date','-start_date']
        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if not self.end_date:
            return None
        else:
            return self.end_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
            return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if not self.end_date:
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])
    
    def __str__(self):
        return self.__unicode__()

class Highlight(SortableMixin):
    description = models.TextField()
    #job = models.ForeignKey(Job)
    job = SortableForeignKey(Work, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])
    
    def __str__(self):
        return self.__unicode__()

class VolunteerHighlight(SortableMixin):
    description = models.TextField()
    #job = models.ForeignKey(Job)
    job = SortableForeignKey(Volunteer, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])
    
    def __str__(self):
        return self.__unicode__()

class Skill(SortableMixin):
    name =  models.CharField(max_length=250)
    url = models.URLField('Skill URL', blank=True)
    level = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class SkillKeyword(SortableMixin):
    name = models.CharField(max_length=250)
    skill = SortableForeignKey('Skill', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.skill.name, ' - ', self.name])
    
    def __str__(self):
        return self.__unicode__()

class Language(SortableMixin):
    name = models.CharField(max_length=250)
    fluency = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class Interest(SortableMixin):
    name = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class InterestKeyword(SortableMixin):
    name = models.CharField(max_length=250)
    interest = SortableForeignKey('Interest', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class Reference(SortableMixin):
    name = models.CharField(max_length=250)
    reference = models.TextField()
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
