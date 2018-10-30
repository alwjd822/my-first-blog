#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from reply.models import Reply

# Create your views here.

class ReplyLV(ListView):
    model = Reply

class ReplyDV(DetailView):
    model = Reply


