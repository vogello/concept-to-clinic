# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-14 21:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0009_auto_20180114_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodule',
            name='note',
            field=models.TextField(help_text='Any notes on the case', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='nodule',
            name='probability_concerning',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]
