# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20160805_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
