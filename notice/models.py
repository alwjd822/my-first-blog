from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from datetime import *
from django.urls import reverse


@python_2_unicode_compatible
class Notice(models.Model):
    nname = models.CharField('제목',max_length=50,null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    ndetails = models.TextField('내용')

    class Meta:
        ordering = ['-pk'] # 최근등록순

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nname

