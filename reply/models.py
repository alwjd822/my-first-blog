from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from course.models import Course
from accounts.models import Profile

# Create your models here.
@python_2_unicode_compatible
class Reply(models.Model): # 댓글
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rdatetime = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    rdetails = models.TextField('내용',null=True)

    class Meta:
        ordering = ['rdatetime']

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
