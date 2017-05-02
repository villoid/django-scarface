# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scarface', '0005_device_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushmessage',
            name='category',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='has_mutable_content',
            field=models.BooleanField(default=False),
        ),
    ]
