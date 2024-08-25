from portfolio import models
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from portfolio.forms import ProjectForm

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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    template_name = 'portfolio/project_form.html'
    success_url = reverse_lazy('my-portfolio')
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)