from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import BasicInfo

admin.site.register(BasicInfo, SingleModelAdmin)