# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-20 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0022_auto_20180206_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposicao',
            name='hash_code',
            field=models.CharField(blank=True, max_length=200, verbose_name='Código do Documento'),
        ),
    ]
