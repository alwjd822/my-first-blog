from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('user', 'name', 'tel', 'address', 'birth')
    list_filter = ('lecturer', 'address', 'birth')
    pass

