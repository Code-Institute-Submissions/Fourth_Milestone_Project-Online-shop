# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-20 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191120_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]