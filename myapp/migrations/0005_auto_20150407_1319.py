# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150407_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=b'1', to='myapp.SubCategory'),
            preserve_default=True,
        ),
    ]
