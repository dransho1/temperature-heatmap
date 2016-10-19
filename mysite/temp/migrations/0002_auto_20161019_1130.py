# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='feed_text',
            new_name='feed_name',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='sensor_text',
            new_name='sensor_name',
        ),
        migrations.AlterField(
            model_name='feed',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
