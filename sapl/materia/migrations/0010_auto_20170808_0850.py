# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-08 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0009_auto_20170712_0951'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='autoria',
            unique_together=set([('autor', 'materia')]),
        ),
    ]