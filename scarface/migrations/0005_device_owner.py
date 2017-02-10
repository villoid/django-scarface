# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scarface', '0004_auto_20151217_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
    ]
