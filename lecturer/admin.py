from django.contrib import admin
from lecturer.models import Lecturer

# Register your models here.

class LecturerAdmin(admin.ModelAdmin):
    list_display  = ('name','bank','account')

admin.site.register(Lecturer, LecturerAdmin)
