# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-17 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0045_auto_20190830_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestingnode',
            name='timezone',
            field=models.CharField(default='America/Buenos_Aires', max_length=100),
        ),
    ]
