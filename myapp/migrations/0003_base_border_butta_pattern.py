# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150413_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('mask_suit', models.ImageField(upload_to=b'base/')),
                ('mask_model', models.ImageField(upload_to=b'base/')),
                ('mask_sideborder', models.ImageField(upload_to=b'base/')),
                ('mask_neckborder', models.ImageField(upload_to=b'base/')),
                ('mask_bottomborder', models.ImageField(upload_to=b'base/')),
                ('image', models.ImageField(upload_to=b'base/')),
                ('baseID', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Border',
            fields=[
                ('image', models.ImageField(upload_to=b'border/')),
                ('borderID', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Butta',
            fields=[
                ('image', models.ImageField(upload_to=b'butta/')),
                ('buttaID', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('image', models.ImageField(upload_to=b'pattern/')),
                ('patternID', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
