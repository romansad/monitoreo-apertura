# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-07 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_auto_20181205_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicadorFederador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('jurisdiccion_nombre', models.CharField(max_length=300)),
                ('jurisdiccion_id', models.CharField(max_length=100, null=True)),
                ('indicador_valor', models.TextField()),
                ('indicador_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.IndicatorType')),
            ],
            options={
                'verbose_name_plural': 'Indicadores nodos federadores',
            },
        ),
    ]
