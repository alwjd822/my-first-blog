'''from django import forms
from .models import Lecturer

class PostForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['bank', 'account', 'career', 'certification', 'profilephoto', 'idphoto']
'''
from django import forms
from lecturer.models import Lecturer

class PostForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['profilephoto', 'idphoto', 'bank', 'account', 'career', 'certification'],

