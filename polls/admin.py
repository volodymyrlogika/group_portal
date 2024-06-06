from django.contrib import admin
from polls.models import Poll, Question, Option, UserPollResult

# Register your models here.


class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "created_by")

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "max_points", "poll")


class OptionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "is_correct", "question")


class UserPollResultAdmin(admin.ModelAdmin):
    list_display = ("id", "completed_by", "poll", "score", "completed_at")


admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserPollResult)
