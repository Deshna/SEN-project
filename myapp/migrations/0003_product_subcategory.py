# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_subcategory_subcategoryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=b'Embroidery', to='myapp.SubCategory'),
            preserve_default=True,
        ),
    ]
