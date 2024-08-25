from django.contrib import admin
from unfold.admin import ModelAdmin

from announcements.models import Announcement

# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    pass