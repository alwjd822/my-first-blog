# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-04 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='ndate',
        ),
        migrations.AddField(
            model_name='notice',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
