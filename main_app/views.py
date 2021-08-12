from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView

from django.http import HttpResponse
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
class Dogs:
    
    def __init__(self, breed, image, bio):
        self.breed = breed
        self.image = image
        self.bio = bio

class DogList(TemplateView):
        template_name = "dog_list.html"

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["dogs"] = [] # this is where we add the key into our context object for the view to use
                return context