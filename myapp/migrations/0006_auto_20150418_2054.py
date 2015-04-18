# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150418_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
