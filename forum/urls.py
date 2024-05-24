from django.urls import path
from forum import views

urlpatterns = [
    path("", views.BranchListView.as_view(), name="branch-list"),
    path("<int:pk>/", views.BranchDetailView.as_view(), name="branch-detailed"),
    path("create_branch/", views.BranchCreateView.as_view(), name="create-branch")
]


app_name = "forum"
