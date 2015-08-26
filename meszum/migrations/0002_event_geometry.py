# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True),
        ),
    ]
