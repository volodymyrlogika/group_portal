from django.shortcuts import render
from forum.models import Branch, Comment
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.

class BranchListView(ListView):
    model = Branch
    context_object_name = "branches"
    template_name = "forum/branches_list.html"


class BranchDetailView(DetailView):
    model = Branch
    context_object_name = "branch"
    template_name = "forum/branch_detail.html"
