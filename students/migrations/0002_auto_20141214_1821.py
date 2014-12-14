# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0003_course_venue'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_color', models.CharField(max_length=35, choices=[(b'RED', b'red'), (b'WHITE', b'white'), (b'BLACK', b'black'), (b'WHITE', b'white'), (b'GREEN', b'green')])),
                ('address', models.ForeignKey(to='address.Address')),
                ('unlike_course', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
    ]
