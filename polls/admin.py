from django.contrib import admin
from polls.models import Poll, Question, Option, UserPollResult

from unfold.admin import ModelAdmin

@admin.register(Poll)
class PollAdmin(ModelAdmin):
    list_display = ("id", "title", "created_at", "created_by")


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("id", "question", "max_points", "poll")


@admin.register(Option)
class OptionAdmin(ModelAdmin):
    list_display = ("id", "text", "is_correct", "question")


@admin.register(UserPollResult)
class UserPollResultAdmin(ModelAdmin):
    list_display = ("id", "completed_by", "poll", "score", "completed_at")

