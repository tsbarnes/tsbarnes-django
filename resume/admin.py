from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from adminsortable.admin import SortableAdmin

from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill

class AccomplishmentAdmin(SortableAdmin):
    list_display = ('job', 'description')

class SkillAdmin(SortableAdmin):
    list_display = ('skillset', 'name')

admin.site.register(Overview, SingleModelAdmin)
admin.site.register(PersonalInfo, SingleModelAdmin)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Accomplishment, AccomplishmentAdmin)
admin.site.register(Skillset, SortableAdmin)
admin.site.register(Skill, SkillAdmin)
