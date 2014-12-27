# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.DateField()),
                ('total', models.IntegerField()),
                ('cycle', models.DateField(null=True, blank=True)),
                ('approvedDate', models.DateTimeField(null=True, blank=True)),
                ('worker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('offDay', models.NullBooleanField()),
                ('worker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
