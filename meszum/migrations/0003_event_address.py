# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0002_event_geometry'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
