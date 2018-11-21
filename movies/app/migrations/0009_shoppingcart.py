# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181119_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=26, max_length=10)),
                ('quantity', models.IntegerField(default=1, max_length=5)),
                ('paystatus', models.BooleanField(default=True)),
                ('seats', models.CharField(max_length=50)),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movies')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'db_table': 'mv_shopping',
            },
        ),
    ]
