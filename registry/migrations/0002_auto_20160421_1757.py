# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]