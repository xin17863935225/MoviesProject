# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-15 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('downloadlink', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mv_movies',
            },
        ),
    ]