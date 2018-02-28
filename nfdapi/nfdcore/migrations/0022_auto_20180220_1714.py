# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfdcore', '0021_jsonfield_20180213_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementspecies',
            name='mushroom_group',
        ),
        migrations.AddField(
            model_name='fungusdetails',
            name='mushroom_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nfdcore.MushroomGroup'),
        ),
    ]