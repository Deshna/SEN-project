# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_mailinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='mail',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
