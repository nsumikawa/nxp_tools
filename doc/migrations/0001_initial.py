# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-08 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name=b'date published')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, max_length=5000, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=b'date viewed')),
                ('Document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Element'),
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.DocumentType'),
        ),
        migrations.AddField(
            model_name='category',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Tool'),
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Type'),
        ),
    ]