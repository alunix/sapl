# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-08 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0055_auto_20190816_0943'),
        ('audiencia', '0012_audienciapublica_parlamentar'),
    ]

    operations = [
        migrations.AddField(
            model_name='audienciapublica',
            name='requerimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requerimento', to='materia.MateriaLegislativa', verbose_name='Requerimento Autor da Audiência Pública'),
        ),
        migrations.AlterField(
            model_name='audienciapublica',
            name='parlamentar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Parlamentar', verbose_name='Parlamentar Autor da Audiência Pública'),
        ),
    ]
