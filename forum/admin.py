from django.contrib import admin
from unfold.admin import ModelAdmin

from forum.models import Branch, Comment

# Register your models here.
@admin.register(Branch)
class BranchAdminClass(ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdminClass(ModelAdmin):
    pass

