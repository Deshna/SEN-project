# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20150411_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_products',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='myapp.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
