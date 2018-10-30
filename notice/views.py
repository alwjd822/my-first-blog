from django.shortcuts import render
#from django.http import HttpResponse

from django.views.generic import ListView, DetailView
#from django.views.generic import TemplateView
from notice.models import Notice

# Create your views here.

class NoticeLV(ListView):
    model = Notice
    paginate_by = 15

class NoticeDV(DetailView):
    model = Notice
"""
class NoticeView(TemplateView):
    template_name = 'notice/notice.html'

#def notice(request):
    #return render(request, 'notice/notice.html')

"""
