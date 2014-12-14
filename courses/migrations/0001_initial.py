# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('technology', models.CharField(max_length=255, choices=[(b'p', b'Python'), (b'r', b'Ruby'), (b'j', b'JavaScript')])),
                ('assistant', models.ForeignKey(related_name='course_assistant', blank=True, to='coaches.Coach', null=True)),
                ('coach', models.ForeignKey(to='coaches.Coach')),
                ('venue', models.ForeignKey(blank=True, to='address.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
