from django.urls import path, include

from portfolio import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='my-portfolio'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-page'),
    path('project/create', views.ProjectCreateView.as_view(), name='project-create'),

]
