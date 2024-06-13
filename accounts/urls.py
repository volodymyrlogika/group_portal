from django.conf.urls import handler403
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts import views

handler403 = views.custom_403_view

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

app_name = 'accounts'