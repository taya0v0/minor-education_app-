from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_program, name="add_program"),
    path("programs/", views.program_list, name="program_list"),
    path("statistics/", views.statistics, name="statistics"),
]
