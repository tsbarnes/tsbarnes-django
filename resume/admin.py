from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from adminsortable.admin import SortableAdmin

from .models import Basics, Location, Profile, Education, Work, Volunteer, Highlight, VolunteerHighlight, Skillset, Skill

class HighlightAdmin(SortableAdmin):
    list_display = ('job', 'description')

class SkillAdmin(SortableAdmin):
    list_display = ('skillset', 'name')

admin.site.register(Basics, SingleModelAdmin)
admin.site.register(Profile, SortableAdmin)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Volunteer)
admin.site.register(Highlight, HighlightAdmin)
admin.site.register(VolunteerHighlight, HighlightAdmin)
admin.site.register(Skillset, SortableAdmin)
admin.site.register(Skill, SkillAdmin)
