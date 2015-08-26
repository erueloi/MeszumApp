# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0003_event_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name='longitude/latitude', blank=True),
        ),
    ]
