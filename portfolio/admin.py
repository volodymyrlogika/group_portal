from django.contrib import admin
from unfold.admin import ModelAdmin

from portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ("id", "title")
