from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('events/', views.events, name='events'),
    path('research_papers/', views.research_papers, name='research_papers'),
]