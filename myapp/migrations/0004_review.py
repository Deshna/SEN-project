# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_base_border_butta_pattern'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='myapp.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
