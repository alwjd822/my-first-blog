from django.contrib import admin
from enrol.models import Enrol,Pay

# Register your models here.

class EnrolAdmin(admin.ModelAdmin):
    list_display  = ('student','course','enroldate')

class PayAdmin(admin.ModelAdmin):
    list_display  = ('pnumber','paymethod')
    
admin.site.register(Enrol, EnrolAdmin)
admin.site.register(Pay, PayAdmin)
