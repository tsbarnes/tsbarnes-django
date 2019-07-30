from django.contrib import admin

from .models import Article


class TinyMCEAdmin(admin.ModelAdmin):
  class Media:
    js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)

admin.site.register(Article, TinyMCEAdmin)