from django.views.generic import ListView
from course.models import Course
from django.db.models import Q 
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# course_lfield_list
class CourseL1LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.1.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 1)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 1).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 1, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 1).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 1).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 1).order_by('-pk')
            return course

class CourseL2LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.2.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 2)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 2).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 2, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 2).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 2).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 2).order_by('-pk')
            return course

class CourseL3LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.3.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 3)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 3).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 3, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 3).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 3).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 3).order_by('-pk')
            return course

class CourseL4LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.4.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 1)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 4).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 4, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 4).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 4).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 4).order_by('-pk')
            return course

class CourseL5LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.5.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 6)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 5).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 5, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 5).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 5).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 5).order_by('-pk')
            return course

class CourseL6LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.6.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 6)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 6).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 6, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 6).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 6).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 6).order_by('-pk')
            return course

class CourseL7LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.7.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__lfield__lnumber = 7)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__lfield__lnumber = 7).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__lfield__lnumber = 7, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 7).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__lfield__lnumber = 7).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__lfield__lnumber = 7).order_by('-pk')
            return course

# course_sfield_list
class CourseS10LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.10.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 10)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 10).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 10, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 10).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 10).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 10).order_by('-pk')
            return course

class CourseS11LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.11.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 11)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 11).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 11, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 11).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 11).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 11).order_by('-pk')
            return course

class CourseS12LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.12.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 12)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 12).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 12, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 12).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 12).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 12).order_by('-pk')
            return course

class CourseS13LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.13.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 13)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 13).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 13, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 13).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 13).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 13).order_by('-pk')
            return course

class CourseS14LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.14.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 14)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 14).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 14, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 14).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 14).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 14).order_by('-pk')
            return course

class CourseS15LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.15.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 15)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 15).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 15, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 15).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 15).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 15).order_by('-pk')
            return course

class CourseS16LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.16.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 16)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 16).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 16, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 16).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 16).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 16).order_by('-pk')
            return course

class CourseS20LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.20.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 20)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 20).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 20, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 20).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 20).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 20).order_by('-pk')
            return course

class CourseS21LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.21.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 21)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 21).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 21, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 21).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 21).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 21).order_by('-pk')
            return course

class CourseS22LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.22.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 22)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 22).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 22, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 22).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 22).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 22).order_by('-pk')
            return course

class CourseS23LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.23.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 23)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 23).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 23, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 23).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 23).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 23).order_by('-pk')
            return course

class CourseS24LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.24.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 24)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 24).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 24, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 24).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 24).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 24).order_by('-pk')
            return course

class CourseS25LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.25.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 25)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 25).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 25, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 25).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 25).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 25).order_by('-pk')
            return course

class CourseS30LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.30.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 30)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 30).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 30, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 30).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 30).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 30).order_by('-pk')
            return course

class CourseS31LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.31.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 31)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 31).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 31, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 31).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 31).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 31).order_by('-pk')
            return course

class CourseS32LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.32.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 32)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 32).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 32, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 32).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 32).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 32).order_by('-pk')
            return course

class CourseS33LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.33.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 33)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 33).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 33, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 33).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 33).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 33).order_by('-pk')
            return course

class CourseS34LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.34.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 34)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 34).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 34, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 34).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 34).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 34).order_by('-pk')
            return course

class CourseS35LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.35.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 35)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 35).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 35, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 35).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 35).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 35).order_by('-pk')
            return course

class CourseS36LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.36.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 36)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 36).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 36, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 36).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 36).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 36).order_by('-pk')
            return course

class CourseS40LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.40.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 40)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 40).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 40, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 40).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 40).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 40).order_by('-pk')
            return course

class CourseS41LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.41.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 41)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 41).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 41, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 41).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 41).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 41).order_by('-pk')
            return course

class CourseS42LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.42.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 42)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 42).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 42, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 42).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 42).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 42).order_by('-pk')
            return course

class CourseS43LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.43.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 43)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 43).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 43, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 43).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 43).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 43).order_by('-pk')
            return course

class CourseS44LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.44.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 44)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 44).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 44, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 44).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 44).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 44).order_by('-pk')
            return course

class CourseS45LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.45.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 45)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 45).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 45, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 45).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 45).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 45).order_by('-pk')
            return course

class CourseS46LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.46.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 46)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 46).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 46, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 46).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 46).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 46).order_by('-pk')
            return course

class CourseS50LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.50.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 50)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 50).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 50, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 50).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 50).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 50).order_by('-pk')
            return course

class CourseS51LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.51.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 51)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 51).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 51, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 51).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 51).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 51).order_by('-pk')
            return course

class CourseS52LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.52.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 52)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 52).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 52, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 52).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 52).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 52).order_by('-pk')
            return course

class CourseS60LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.60.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 60)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 60).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 60, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 60).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 60).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 60).order_by('-pk')
            return course

class CourseS61LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.61.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 61)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 61).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 61, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 61).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 61).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 61).order_by('-pk')
            return course

class CourseS62LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.62.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 62)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 62).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 62, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 62).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 62).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 62).order_by('-pk')
            return course

class CourseS63LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.63.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 63)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 63).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 63, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 63).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 63).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 63).order_by('-pk')
            return course

class CourseS64LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.64.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 64)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 64).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 64, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 64).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 64).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 64).order_by('-pk')
            return course

class CourseS70LV(ListView):
    model = Course
    paginate_by = 20
    template_name = 'course/course_list.70.html'

    def get_queryset(self):
        qs = Course.objects.filter(sfield__snumber = 70)
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort','')
        if q:
            qs = qs.filter(Q(name__name__name__icontains=q) | Q(cname__icontains=q) | Q(place__icontains=q) | Q(sfield__sname__icontains=q)).distinct()
            return qs
        elif sort == 'likes':
            course = Course.objects.filter(sfield__snumber = 70).annotate(like_count=Count('likes')).order_by('-like_count', '-pk')
            return course
        elif sort == 'mypost':
            user = self.request.user.profile.lecturer
            course = Course.objects.filter(sfield__snumber = 70, name = user.id).order_by('-pk') #복수를 가져올수 있음
            return course
        elif sort == 'high_cost':
            course = Course.objects.filter(sfield__snumber = 70).order_by('-cost', '-pk') #복수를 가져올수 있음
            return course
        elif sort == 'low_cost':
            course = Course.objects.filter(sfield__snumber = 70).order_by('cost', '-pk') #복수를 가져올수 있음
            return course
        else:
            course = Course.objects.filter(sfield__snumber = 70).order_by('-pk')
            return course