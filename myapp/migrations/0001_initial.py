# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('categoryID', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.IntegerField(serialize=False, primary_key=True)),
                ('customerID', models.IntegerField()),
                ('orderDate', models.IntegerField()),
                ('shipperID', models.IntegerField()),
                ('billID', models.IntegerField()),
                ('totalprice', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.ForeignKey(to='myapp.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('path', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('productID', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(default=b'none', max_length=300)),
                ('unitsInStock', models.IntegerField(default=0)),
                ('unitsInOrder', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=10)),
                ('work', models.CharField(default=b'none', max_length=30)),
                ('fabric', models.CharField(default=b'', max_length=30, null=True, blank=True)),
                ('style', models.CharField(default=b'', max_length=30, null=True, blank=True)),
                ('occasion', models.CharField(default=b'', max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('category', models.ForeignKey(to='myapp.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='productID',
            field=models.OneToOneField(to='myapp.Product'),
            preserve_default=True,
        ),
    ]
