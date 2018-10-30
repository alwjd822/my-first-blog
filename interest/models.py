from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from course.models import Course
from accounts.models import Profile

@python_2_unicode_compatible
class Interest(models.Model): # 관심
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['course']
