# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-10 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0026_auto_20180302_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialegislativa',
            name='numero_origem_externa',
            field=models.CharField(blank=True, max_length=10, verbose_name='Número'),
        ),
    ]
