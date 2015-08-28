# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def make_groups(apps,schema_editor):
    Group = apps.get_model("auth","Group")
    Group.objects.create(name="Space")
    Group.objects.create(name="Member")
    Group.objects.create(name="DJ")

class Migration(migrations.Migration):

    dependencies = [
        ('meszum', '0004_auto_20150822_1825'),
    ]

    operations = [
        migrations.RunPython(make_groups),
    ]
