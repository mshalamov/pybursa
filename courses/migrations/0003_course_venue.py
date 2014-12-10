# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0002_auto_20141208_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(blank=True, to='address.Address', null=True),
            preserve_default=True,
        ),
    ]
