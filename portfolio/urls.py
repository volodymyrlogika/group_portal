from django.urls import path, include

from portfolio import views

urlpatterns = [
    path('my-portfolio/', views.ProjectListView.as_view(), name='my-portfolio'),
    path('my-portfolio/project/<int:pk>', views.ProjectDetailView.as_view(), name='project-page')

]
