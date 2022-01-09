from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.login),
    path("register/", views.register),
    path("dashboard/", views.dashboard),
    path("profile/", views.profile),
    path("create_story/", views.create_story)
]