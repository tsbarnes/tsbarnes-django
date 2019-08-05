from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from adminsortable.admin import SortableAdmin

from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill

admin.site.register(Overview, SingleModelAdmin)
admin.site.register(PersonalInfo, SingleModelAdmin)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Accomplishment, SortableAdmin)
admin.site.register(Skillset, SortableAdmin)
admin.site.register(Skill, SortableAdmin)
