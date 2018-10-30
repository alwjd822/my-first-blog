from django.views.generic import ListView, DetailView
from course.models import Course, Schedule
from .models import Course
from lecturer.models import Lecturer
from course.forms import ScheduleInlineFormSet, ScheduleUVInlineFormSet, GalleryInlineFormSet, GalleryUVInlineFormSet

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from mysite.views import LoginRequiredMixin

from django.db.models import Q 
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse  
from django.db.models import Count

class CourseLV(ListView):
    model = Course
    paginate_by = 20

    def get_queryset(self):
        qs = Course.objects.all()
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.order_by('-pk')
            return course

class CourseDV(DetailView):
    model = Course

class LecturerDV(DetailView) :
    model = Course
    template_name = 'course/lecturer_detail.html'

    #def form_valid(self, form):
        #form.instance.name = get_object_or_404(Course, pk=self.kwargs['course_lecturer_pk'])
        #return super(LecturerDV, self).form_valid(form)

class CourseScheduleCV(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['cname', 'cost', 'startdate', 'enddate', 'sfield', 'minperson', 'maxperson', 'place', 'image', 'details']
    
    def get_context_data(self, **kwargs):
        context = super(CourseScheduleCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ScheduleInlineFormSet(self.request.POST, self.request.FILES)
            context['gallery_formset'] = GalleryInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = ScheduleInlineFormSet()
            context['gallery_formset'] = GalleryInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.name = self.request.user.profile.lecturer
        context = self.get_context_data()
        formset = context['formset']
        gallery_formset = context['gallery_formset']
        for scheduleform in formset:
            scheduleform.instance.name = self.request.user.profile.lecturer
        for galleryform in gallery_formset:
            galleryform.instance.name = self.request.user.profile.lecturer
        if formset.is_valid() and gallery_formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            gallery_formset.instance = self.object
            gallery_formset.save()
            return redirect('course:change')
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CourseChangeLV(LoginRequiredMixin, ListView):
    template_name = 'course/course_change_list.html'
    paginate_by = 15

    def get_queryset(self):
        return Course.objects.filter(name=self.request.user.profile.lecturer)

class CourseUpdateView(LoginRequiredMixin, UpdateView) :
    model = Course
    fields = ['cname', 'cost', 'startdate', 'enddate', 'sfield', 'minperson', 'maxperson', 'place', 'image', 'details']
    template_name = 'course/course_change_form.html'
    success_url = reverse_lazy('course:change')

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ScheduleUVInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['gallery_formset'] = GalleryUVInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = ScheduleUVInlineFormSet(instance=self.object)
            context['gallery_formset'] = GalleryUVInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        gallery_formset = context['gallery_formset']
        if formset.is_valid() and gallery_formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            gallery_formset.instance = self.object
            gallery_formset.save()
            return redirect('course:change')
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CourseDeleteView(LoginRequiredMixin, DeleteView) :
    model = Course
    success_url = reverse_lazy('course:change')

@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user.profile # 로그인한 유저를 가져온다.
        cname = request.POST.get('pk', None)
        course = Course.objects.get(pk = cname) #해당 메모 오브젝트를 가져온다.

        if course.likes.filter(id = user.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            course.likes.remove(user) #likes 컬럼에서 해당 유저를 지운다.
            message = '좋아요 취소'
        else:
            course.likes.add(user)
            message = '좋아요 확인'+'\n'+'\n'+'[마이페이지]-[관심 내역]에서 확인하세요!'  

    context = {'likes_count' : course.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')
    # dic 형식을 json 형식으로 바꾸어 전달한다.

class LikesLV(LoginRequiredMixin, ListView):
    template_name = 'course/likes_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Course.objects.filter(likes=self.request.user.profile)
