from django.shortcuts import render

from django.views.generic import ListView, DetailView
#from django.views.generic import TemplateView
from interest.models import Interest

# Create your views here.

class InterestLV(ListView):
    model = Interest

class InterestDV(DetailView):
    model = Interest
