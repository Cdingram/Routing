# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20161002_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=250),
        ),
    ]