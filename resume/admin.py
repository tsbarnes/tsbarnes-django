from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from adminsortable.admin import SortableAdmin

from .models import Basics, Location, Profile, Education, Work, Volunteer, Highlight, VolunteerHighlight, Skill, SkillKeyword

class HighlightAdmin(SortableAdmin):
    list_display = ('job', 'description')

admin.site.register(Basics, SingleModelAdmin)
admin.site.register(Location)
admin.site.register(Profile, SortableAdmin)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Volunteer)
admin.site.register(Highlight, HighlightAdmin)
admin.site.register(VolunteerHighlight, HighlightAdmin)
admin.site.register(Skill, SortableAdmin)
admin.site.register(SkillKeyword, SortableAdmin)
