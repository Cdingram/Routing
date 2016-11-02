# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=250)),
                ('city', models.TextField(max_length=250)),
                ('province', models.CharField(choices=[('AB', 'Alberta')], default='AB', max_length=2)),
                ('postal_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
    ]
