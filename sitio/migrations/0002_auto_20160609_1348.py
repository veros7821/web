# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-09 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]