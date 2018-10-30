from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

from course.models import Course
from accounts.models import Profile

@python_2_unicode_compatible
class Enrol(models.Model): # 수강
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    paymethod = models.ForeignKey('Pay', on_delete=models.CASCADE)
    #paycost = models.IntegerField('결제가격',default=0)
    paydate = models.DateField(auto_now=False, auto_now_add=False,null=True)
    enroldate = models.DateField(auto_now=False, auto_now_add=False,null=True)

    class Meta:
        ordering = ['course']

    #def paycost(self):  # 합계 점수
        #return self.enrol.course.cost * 0.5

@python_2_unicode_compatible
class Pay(models.Model):
    pnumber = models.IntegerField('결제번호')
    paymethod = models.CharField('결제방법',max_length=50)

    class Meta:
        ordering = ['paymethod']

    def __str__(self):
        return self.paymethod
