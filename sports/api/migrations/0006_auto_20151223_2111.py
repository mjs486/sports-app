# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151222_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athletes', to='api.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='api.Sport'),
        ),
    ]
