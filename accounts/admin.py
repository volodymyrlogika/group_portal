from django.contrib import admin

from accounts.models import Role, UserProfile

# Register your models here.
admin.site.register(Role)
admin.site.register(UserProfile)
