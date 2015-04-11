# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20150407_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
