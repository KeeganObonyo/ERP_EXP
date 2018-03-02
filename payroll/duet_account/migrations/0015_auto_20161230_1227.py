# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duet_account', '0014_auto_20161230_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarysheet',
            name='account_number',
            field=models.CharField(max_length=20, null=True, verbose_name='Account Number'),
        ),
        migrations.AddField(
            model_name='salarysheet',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='duet_account.Grade', verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='salaryscale',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
