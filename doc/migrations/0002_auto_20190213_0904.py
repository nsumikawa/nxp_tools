# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-13 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=b'date published'),
        ),
    ]
