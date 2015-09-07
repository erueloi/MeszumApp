# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0010_auto_20150907_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='href_play',
            field=models.CharField(default=0, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
