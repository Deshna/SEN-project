# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20150410_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.CommaSeparatedIntegerField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
