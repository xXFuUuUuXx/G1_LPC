# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compromisso',
            name='institucinal',
        ),
        migrations.AddField(
            model_name='agenda',
            name='instiutucial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agenda',
            name='share_with',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='fk_agendacompartilhada', to='agenda.Usuario'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Agenda_Institucional',
        ),
    ]
