from django.views.generic import ListView, DetailView
from enrol.models import Enrol, Pay
from course.models import Course
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.

class EnrolLV(LoginRequiredMixin, ListView):
    model = Enrol
    paginate_by = 6

    def get_queryset(self):
        return Enrol.objects.filter(student=self.request.user.profile)

#class EnrolDV(DetailView):
    #model = Enrol
    #template_name = 'enrol/enrol_detail.html'

class EnrolCreateView(LoginRequiredMixin, CreateView):
    model = Enrol
    fields = ['paymethod']
    success_url = reverse_lazy('enrol:index')

    def get_object(self):
        return self.request.course

    def form_valid(self, form):
        form.instance.student = self.request.user.profile
        form.instance.course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        return super(EnrolCreateView, self).form_valid(form)

#class EnrolChangeLV(LoginRequiredMixin, ListView):
#    template_name = 'enrol/enrol_list.html'

#    def get_queryset(self):
#        return Enrol.objects.filter(name=self.request.user.profile.lecturer.course)

class EnrolStudentLV(LoginRequiredMixin, ListView):
    model = Enrol
    template_name = 'enrol/enrol_student.html'
    paginate_by = 15

    def get_queryset(self):
        return Enrol.objects.filter(student=self.request.user.profile)
