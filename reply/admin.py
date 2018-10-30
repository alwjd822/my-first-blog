from django.contrib import admin
from reply.models import Reply

# Register your models here.

class ReplyAdmin(admin.ModelAdmin):
    list_display  = ('course','name','rdatetime','rdetails')

admin.site.register(Reply, ReplyAdmin)
