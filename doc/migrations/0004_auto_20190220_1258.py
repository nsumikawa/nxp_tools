# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-20 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_auto_20190220_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date viewed'),
        ),
    ]
