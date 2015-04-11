# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='SubCategory',
            field=models.ForeignKey(to='myapp.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
