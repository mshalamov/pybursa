# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=5, blank=True)),
                ('country', models.CharField(max_length=100, blank=True)),
                ('province', models.CharField(max_length=100, blank=True)),
                ('district', models.CharField(max_length=100, blank=True)),
                ('street', models.CharField(max_length=100, blank=True)),
                ('house', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
