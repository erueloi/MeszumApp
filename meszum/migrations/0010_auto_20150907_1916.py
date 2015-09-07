# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0009_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=254),
        ),
    ]
