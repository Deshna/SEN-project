# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=b'Machine', to='myapp.SubCategory'),
            preserve_default=True,
        ),
    ]
