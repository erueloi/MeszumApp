# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0008_auto_20150903_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('artist', models.EmailField(max_length=254)),
                ('album', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(to='meszum.Event')),
            ],
        ),
    ]
