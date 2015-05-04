# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='product',
            field=models.ManyToManyField(to='myapp.Product', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='product',
            field=models.ManyToManyField(to='myapp.Product', null=True, blank=True),
        ),
    ]
