# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 22:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frisor_urls', '0002_auto_20170316_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='creator',
            new_name='nick',
        ),
    ]
