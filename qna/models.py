from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

@python_2_unicode_compatible
class Qna(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('제목',max_length=50,null=True)
    createdate = models.DateTimeField('생성일자',auto_now_add=True, null=True)
    modifydate = models.DateTimeField('수정일자',auto_now=True,null=True)
    details = models.TextField('내용')

    class Meta:
        ordering = ['-pk'] # 최근등록순

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail')

    #def createdate_in(self):
    #    return self.createdate.strftime('%Y-%m-%d %H:%M')
    #createdate_in.short_description = 'createdate decade'

    
    
