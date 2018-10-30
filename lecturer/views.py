from django.shortcuts import redirect, render
from lecturer.models import Lecturer
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class LecturerLV(ListView):
    model = Lecturer
'''
class LecturerDV(DetailView) :
    model = Lecturer

    def get_object(self):
        return self.request.lecturer

    def form_valid(self, form):
        form.instance.name = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        return super(LecturerDV, self).form_valid(form)

    #def form_valid(self, form):
        #form.instance.name = get_object_or_404(Course, pk=self.kwargs['course_lecturer_pk'])
        #return super(LecturerDV, self).form_valid(form)
'''
class LecturerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Lecturer
    fields = ['profilephoto', 'idphoto', 'bank', 'account', 'career', 'certification']
    success_url = reverse_lazy('accounts:profile')
    success_message = '강사 신청이 완료되었습니다.'+'\n'+ '등록 완료까지 1~3일이 소요됩니다.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LecturerCreateView, self).form_valid(form)

#   def form_valid(self, form):
#        form.instance.user = self.request.user
#        user = self.cleaned_data['user']
#        if Lecturer.objects.filter(lecturer__user=user).exists():
#            raise forms.ValidationError('이미 등록되었습니다')
#        return super(LecturerCreateView, self).form_valid(form)

    # username필드의 검증에 username이 이미 사용중인지 여부 검사
#    def clean_user(self):
#        user = self.cleaned_data['user']
#        if Lecturer.objects.filter(user=user).exists():
#            raise forms.ValidationError('이미 등록되었습니다')
#        return user

class LecturerUpdateView(LoginRequiredMixin, UpdateView) :
    model = Lecturer
    fields = ['profilephoto', 'idphoto', 'bank', 'account', 'career', 'certification']
    template_name = 'lecturer/lecturer_change_form.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user.profile.lecturer

class LecturerDeleteView(LoginRequiredMixin, DeleteView) :
    model = Lecturer
    success_url = reverse_lazy('accounts:profile')