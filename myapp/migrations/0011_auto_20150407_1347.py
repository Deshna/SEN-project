# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_product_smth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='smth',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(to='myapp.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
