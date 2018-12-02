# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='learning.University'),
        ),
    ]
