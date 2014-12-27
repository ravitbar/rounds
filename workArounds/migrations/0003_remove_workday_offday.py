# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workArounds', '0002_remove_monthlyreport_cycle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workday',
            name='offDay',
        ),
    ]
