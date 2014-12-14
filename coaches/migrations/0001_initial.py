# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=13)),
                ('coach_type', models.CharField(max_length=1, choices=[(b'C', b'Coach'), (b'A', b'Assistant')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
