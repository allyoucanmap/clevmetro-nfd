# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170721_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slimemolddetails',
            name='lifestages',
        ),
        migrations.AddField(
            model_name='slimemoldclass',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='srank',
            name='code',
            field=models.TextField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='srank',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='species',
            name='tsn',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='repository',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
