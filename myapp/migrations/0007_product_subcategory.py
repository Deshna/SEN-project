# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SubCategory',
            field=models.ForeignKey(default=b'1', to='myapp.SubCategory'),
            preserve_default=True,
        ),
    ]
