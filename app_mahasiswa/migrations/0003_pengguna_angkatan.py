# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mahasiswa', '0003_auto_20171213_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengguna',
            name='angkatan',
            field=models.CharField(default=2016, max_length=5, verbose_name='angkatan'),
            preserve_default=False,
        ),
    ]
