from django.urls import path
from forum import views

urlpatterns = [
    path("", views.BranchListView.as_view(), name="branch-list"),
    path("<int:pk>/", views.BranchDetailView.as_view(), name="branch-detailed")
]


app_name = "forum"
