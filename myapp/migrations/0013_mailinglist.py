# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_product_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailinglist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=20, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
