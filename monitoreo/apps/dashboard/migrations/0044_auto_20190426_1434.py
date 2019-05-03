# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_datajsonar', '0006_synchronizer_node'),
        ('dashboard', '0043_auto_20190301_1216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='validationreporttask',
            options={'verbose_name_plural': 'Reportes de validación'},
        ),
        migrations.AddField(
            model_name='federationtask',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node'),
        ),
        migrations.AddField(
            model_name='indicatorsgenerationtask',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node'),
        ),
        migrations.AddField(
            model_name='reportgenerationtask',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node'),
        ),
        migrations.AddField(
            model_name='validationreporttask',
            name='node',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_datajsonar.Node'),
        ),
    ]
