from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from announcements import models
from announcements.forms import AnnouncementForm
from announcements.models import Announcement


# Create your views here.
class AnnouncementsListView(ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'announcements/announcements_list.html'


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = models.Announcement
    template_name = 'announcements/announcement_create.html'
    success_url = reverse_lazy('announcements-list')
    form_class = AnnouncementForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)