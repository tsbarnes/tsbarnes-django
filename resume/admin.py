from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill

admin.site.register(Overview, SingleModelAdmin)
admin.site.register(PersonalInfo, SingleModelAdmin)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Accomplishment)
admin.site.register(Skillset)
admin.site.register(Skill)
