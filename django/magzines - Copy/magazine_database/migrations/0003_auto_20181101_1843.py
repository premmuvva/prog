# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-01 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_database', '0002_remove_customers_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazines',
            name='magazine_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
