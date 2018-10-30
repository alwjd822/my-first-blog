from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User

@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField('이름',max_length=50)
    tel = models.CharField('전화번호',max_length=50)
    #gender = models.BooleanField('성별',default=True)
    address = models.CharField('주소',max_length=50)
    birth = models.DateField('생년월일',auto_now=False, auto_now_add=False,null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def decade_born_in(self):
        return self.birth.strftime('%Y')[:4] # + "0's"
    decade_born_in.short_description = 'Birth decade'

    def born_in_fifties(self):
        return self.birth.strftime('%Y')[:4] == '195'
    born_in_fifties.boolean = True

class User(models.Model):
    username = models.CharField(max_length=191)
    password = models.IntegerField()
 
    def __unicode__(self):
        return self.username


