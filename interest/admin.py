from django.contrib import admin
from interest.models import Interest

# Register your models here.

class InterestAdmin(admin.ModelAdmin):
    list_display  = ('course','name')

admin.site.register(Interest, InterestAdmin)
