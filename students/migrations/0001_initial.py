# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_color', models.CharField(max_length=35, choices=[(b'RED', b'red'), (b'WHITE', b'white'), (b'BLACK', b'black'), (b'GREEN', b'green'), (b'YELLOW', b'yellow')])),
                ('address', models.ForeignKey(to='address.Address')),
                ('unlike_course', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=13, blank=True)),
                ('package', models.CharField(default=b's', max_length=1, choices=[(b's', b'Standard'), (b'g', b'Gold'), (b'p', b'Platinum')])),
                ('courses', models.ManyToManyField(to='courses.Course', blank=True)),
                ('dossier', models.OneToOneField(null=True, blank=True, to='students.Dossier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
