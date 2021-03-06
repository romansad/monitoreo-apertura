# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_tablecolumn'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicadorPAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('indicador_valor', models.CharField(max_length=300)),
                ('indicador_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.IndicatorType')),
            ],
            options={
                'get_latest_by': 'fecha',
                'verbose_name_plural': 'Indicadores del PAD',
            },
        ),
        migrations.AlterModelOptions(
            name='indicadorred',
            options={'get_latest_by': 'fecha', 'verbose_name_plural': 'Indicadores de red'},
        ),
    ]
