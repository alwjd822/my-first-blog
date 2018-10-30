from django.contrib import admin
from course.models import Course, Schedule, Lfield, Sfield, Gallery

# Register your models here.

class ScheduleInline(admin.StackedInline):
    model = Schedule
    extra = 1

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = (ScheduleInline, GalleryInline)
    list_display  = ('id','cname','sfield','name','cost')
    list_display_links = ('id', 'cname')
    # list_editable = ['author'] 목록 상에서 수정할 필드 목록
    search_fields = ('cname', 'details')
    list_filter = ('sfield__lfield','name','cname','cost')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['course']

class LfieldAdmin(admin.ModelAdmin):
    list_display  = ('lname','lnumber')

class SfieldAdmin(admin.ModelAdmin):
    list_display  = ('sname','snumber')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'starttime','endtime')

admin.site.register(Course, CourseAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Lfield, LfieldAdmin)
admin.site.register(Sfield, SfieldAdmin)
admin.site.register(Schedule, ScheduleAdmin)
