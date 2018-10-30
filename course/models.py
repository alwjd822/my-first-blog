from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from course.fields import ThumbnailImageField

from accounts.models import Profile
from lecturer.models import Lecturer

@python_2_unicode_compatible
class Course(models.Model): # 강좌
    sfield = models.ForeignKey('Sfield',on_delete=models.CASCADE,null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.ForeignKey(Lecturer, on_delete=models.CASCADE,null=True)
    cname = models.CharField('Cname',max_length=50)
    cost = models.IntegerField('Cost',default=0)
    startdate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    enddate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    minperson = models.IntegerField('최소인원',default=0)
    maxperson = models.IntegerField('최대인원',default=0)
    place = models.CharField('장소',max_length=50)
    image = ThumbnailImageField(upload_to='course/%Y/%m')
    details = models.TextField('상세정보')
    likes = models.ManyToManyField(Profile, related_name='likes')

    class Meta:
        ordering = ['-pk'] # 최근등록순

    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        return reverse('course:change')

    @property
    def total_likes(self):
        return self.likes.count() #likes 컬럼의 값의 갯수를 센다

@python_2_unicode_compatible
class Gallery(models.Model): # 갤러리
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    image1 = ThumbnailImageField(upload_to='course/%Y/%m')
    image2 = ThumbnailImageField(upload_to='course/%Y/%m')
    image3 = ThumbnailImageField(upload_to='course/%Y/%m')
    image4 = ThumbnailImageField(upload_to='course/%Y/%m')
    name = models.ForeignKey(Lecturer, on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['course']

@python_2_unicode_compatible
class Lfield(models.Model): # 대분류
    lnumber = models.IntegerField('대분류번호',null=True)
    lname = models.CharField('large field',max_length=50)

    class Meta:
        ordering = ['lnumber']
    
    def __str__(self):
        return self.lname

@python_2_unicode_compatible
class Sfield(models.Model): #소분류
    lfield = models.ForeignKey('Lfield',on_delete=models.CASCADE,null=True)
    snumber = models.IntegerField('소분류번호',null=True)
    sname = models.CharField('small field',max_length=50)

    class Meta:
        ordering = ['snumber']
    
    def __str__(self):
        return self.sname

@python_2_unicode_compatible
class Schedule(models.Model): # 일정
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    #day = models.DateField(auto_now=False, auto_now_add=False,null=True)
    starttime = models.TimeField('Starttime',auto_now=False, auto_now_add=False)
    endtime = models.TimeField('Endtime',auto_now=False, auto_now_add=False)
    name = models.ForeignKey(Lecturer, on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['course']

    #def __str__(self): 
    #    return self.course 

    def get_absolute_url(self):
        return reverse('course:change')