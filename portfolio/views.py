from msilib.schema import ListView
from portfolio import models
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin,ListView):
    model = models.Project
    context_object_name = 'projects'
    template_name = 'portfolio/project_list.html'
    
    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = models.Project
    context_object_name = 'project'
    template_name = 'portfolio/project.html'