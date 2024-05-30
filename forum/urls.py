from django.urls import path
from forum import views

urlpatterns = [
    path("", views.BranchListView.as_view(), name="branch-list"),
    path("branch/<int:pk>/", views.BranchDetailView.as_view(), name="branch-detailed"),
    path("create_branch/", views.BranchCreateView.as_view(), name="create-branch"),
    path("branch/<int:pk>/delete/", views.BranchDeleteView.as_view(), name="delete-branch"),
    path("branch/<int:pk>/comment/add/", views.CommentCreateView.as_view(), name="comment-create")
]


app_name = "forum"
