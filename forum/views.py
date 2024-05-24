from django.shortcuts import render
from forum.models import Branch, Comment
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.forms import BranchCreate
from django.urls import reverse_lazy

# Create your views here.


class BranchListView(ListView):
    model = Branch
    context_object_name = "branches"
    template_name = "forum/branches_list.html"
    paginate_by = 10


class BranchDetailView(DetailView):
    model = Branch
    context_object_name = "branch"
    template_name = "forum/branch_detail.html"


class BranchCreateView(LoginRequiredMixin, CreateView):
    model = Branch
    template_name = "forum/branch_form.html"
    form_class = BranchCreate
    success_url = reverse_lazy("forum:branch-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
