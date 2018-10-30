from django.contrib import admin
from notice.models import Notice

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display  = ('nname','published_date')

admin.site.register(Notice, NoticeAdmin)
