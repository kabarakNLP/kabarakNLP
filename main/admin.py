from django.contrib import admin
from main.models import Profile, NLPProject, NLPEvent, ResearchPaper
# Register your models here.

admin.site.register(Profile)
admin.site.register(NLPProject)
admin.site.register(NLPEvent)
admin.site.register(ResearchPaper)