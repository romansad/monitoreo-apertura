# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_federationtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='federationtask',
            name='harvesting_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.HarvestingNode'),
        ),
    ]
