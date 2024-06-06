from django.shortcuts import render, redirect, get_object_or_404
from forum.models import Branch, Comment
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.forms import BranchCreate, CommentForm
from django.urls import reverse_lazy
from forum.mixins import UserIsOwnerMixin

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        return context


class BranchCreateView(LoginRequiredMixin, CreateView):
    model = Branch
    template_name = "forum/branch_form.html"
    form_class = BranchCreate
    success_url = reverse_lazy("forum:branch-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BranchDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Branch
    success_url = reverse_lazy("forum:branch-list")
    template_name = "forum/branch_delete_confirm.html"


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("forum:branch-detailed", kwargs={"pk": self.object.branch.pk})

    def get_branch(self):
        branch_pk = self.kwargs.get("pk")

        return get_object_or_404(Branch, pk=branch_pk)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.branch = self.get_branch()

        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = "forum/comment_delete_confirmation.html"

    def get_success_url(self):
        return reverse_lazy("forum:branch-detailed", kwargs={"pk": self.object.branch.pk})


