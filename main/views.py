from django.shortcuts import render
from .models import NLPProject, NLPEvent, ResearchPaper

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    projects = NLPProject.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def events(request):
    events = NLPEvent.objects.all()
    return render(request, 'main/events.html', {'events': events})

def research_papers(request):
    papers = ResearchPaper.objects.all()
    return render(request, 'main/research_papers.html', {'papers': papers})
