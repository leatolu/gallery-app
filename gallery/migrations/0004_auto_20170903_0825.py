# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20170903_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
