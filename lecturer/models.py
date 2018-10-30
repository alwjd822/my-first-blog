from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from accounts.models import Profile
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from django.contrib.auth.models import User

@python_2_unicode_compatible
class Lecturer(models.Model): # 강사
    user = models.ForeignKey(User)
    name = models.OneToOneField(Profile,on_delete=models.CASCADE,null=True)
    bank = models.CharField('은행명',max_length=50)
    account = models.CharField('계좌번호',max_length=50)
    career = models.TextField('경력사항')
    certification = models.TextField('자격증')
    profilephoto = ProcessedImageField(blank=False, upload_to='lecturer/post/%Y/%m/%d',
             processors=[Thumbnail(300, 300)],
             format='JPEG',
             options={'quality': 60})
    idphoto = ProcessedImageField(blank=False, upload_to='lecturer/post/%Y/%m/%d',
             processors=[Thumbnail(300, 300)],
             format='JPEG',
             options={'quality': 60})
    # 프로필사진, 신분증, 자격증사진(보류) imgfield

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name) #__str__ returned non-string (type Profile) > str()추가

    def get_absolute_url(self):
        #return self.course.get_absolute_url()
        return reverse('course:lecturer', args=[self.id])





