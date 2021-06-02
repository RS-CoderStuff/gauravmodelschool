# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-31 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0041_auto_20200731_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch_db',
            name='category',
        ),
        migrations.AddField(
            model_name='batch_db',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='category', to='ieltsapp.Sub_Course_Category_Db'),
        ),
    ]