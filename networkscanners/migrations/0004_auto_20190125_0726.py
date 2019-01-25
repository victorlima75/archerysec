# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkscanners', '0003_auto_20181101_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='nessus_report_db',
            name='scanner',
            field=models.CharField(default='Nessus', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='ov_scan_result_db',
            name='scanner',
            field=models.CharField(default='OpenVAS', editable=False, max_length=15),
        ),
    ]