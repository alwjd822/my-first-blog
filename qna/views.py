"""#from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from qna.models import Qna

# Create your views here.

class QnaLV(ListView):
    model = Qna

class QnaDV(DetailView):
    model = Qna


class PostLV(ListView) :
    model = Qna
    template_name = 'qna/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
"""
from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

from qna.models import Qna

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

#--- ListView
class PostLV(ListView) :
    model = Qna
    paginate_by = 15
    #context_object_name = 'posts'

#--- DetailView
class PostDV(DetailView) :
    model = Qna

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Qna
    fields = ['title', 'details']
    success_url = reverse_lazy('qna:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'qna/qna_change_list.html'
    paginate_by = 15

    def get_queryset(self):
        return Qna.objects.filter(owner=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView) :
    model = Qna
    fields = ['title', 'details']
    success_url = reverse_lazy('qna:index')

class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Qna
    success_url = reverse_lazy('qna:index')


