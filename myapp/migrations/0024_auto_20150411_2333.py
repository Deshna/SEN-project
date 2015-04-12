# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20150411_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colors', models.CharField(max_length=60)),
                ('product', models.ManyToManyField(to='myapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabrics', models.CharField(max_length=60)),
                ('product', models.ManyToManyField(to='myapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occasions', models.CharField(max_length=60)),
                ('product', models.ManyToManyField(to='myapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pastorders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderno', models.IntegerField()),
                ('user', models.ForeignKey(to='myapp.UserProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('works', models.CharField(max_length=60)),
                ('product', models.ManyToManyField(to='myapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='product',
            name='occasion',
        ),
        migrations.RemoveField(
            model_name='product',
            name='style',
        ),
        migrations.RemoveField(
            model_name='product',
            name='work',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pastorders_no',
        ),
    ]
