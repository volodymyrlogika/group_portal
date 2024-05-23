from django.urls import path

from announcements import views

urlpatterns = [
    path('all/', views.AnnouncementsListView.as_view(), name='announcements-list')
]