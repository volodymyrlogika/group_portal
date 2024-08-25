from django.contrib import admin
from unfold.admin import ModelAdmin

from accounts.models import Role, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(ModelAdmin):
    pass