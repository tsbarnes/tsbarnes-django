from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Project


class TinyMCEAdmin(SortableAdmin):
  class Media:
    js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)

admin.site.register(Project, TinyMCEAdmin)