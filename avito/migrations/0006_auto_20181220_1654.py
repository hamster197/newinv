# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-20 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito', '0005_auto_20181220_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avitoflats',
            name='DateEnd',
            field=models.DateField(verbose_name='Дата окончания публикации объявления:'),
        ),
    ]
