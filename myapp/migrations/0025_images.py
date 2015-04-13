# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20150411_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/home/')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ForeignKey(to='myapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
