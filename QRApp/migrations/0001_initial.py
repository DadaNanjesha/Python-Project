# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-04 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gtin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtin_number', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['gtin_number'],
                'verbose_name': 'GTIN NUMBER',
                'verbose_name_plural': 'GTIN NUMBER',
            },
        ),
    ]
