# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-17 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0045_auto_20190830_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatortype',
            name='panel_federadores',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='panel_nodos',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='indicatortype',
            name='panel_red',
            field=models.BooleanField(default=True),
        ),
    ]
