from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Hero(TemplateView):
    template_name = 'index.html'

class Story(TemplateView):
    template_name = 'story.html'

class Iron(TemplateView):
    template_name = 'iron.html'

class Thor(TemplateView):
    template_name = 'thor.html'

class USA(TemplateView):
    template_name = 'america.html'

