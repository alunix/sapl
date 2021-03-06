# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-31 18:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materia', '0051_auto_20190703_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposicao',
            name='ip',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='IP'),
        ),
        migrations.AddField(
            model_name='proposicao',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
