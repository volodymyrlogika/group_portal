from django.shortcuts import render
from django.views.generic import ListView

from announcements.models import Announcement


# Create your views here.
class AnnouncementsListView(ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'announcements/announcements_list.html'