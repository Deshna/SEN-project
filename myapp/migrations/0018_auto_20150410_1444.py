# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20150409_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.CommaSeparatedIntegerField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pastorders_no',
            field=models.CommaSeparatedIntegerField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
