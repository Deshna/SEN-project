# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
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
        ),
        migrations.CreateModel(
            name='Border',
            fields=[
                ('image', models.ImageField(upload_to=b'border/')),
                ('borderID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Butta',
            fields=[
                ('image', models.ImageField(upload_to=b'butta/')),
                ('buttaID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_products', models.CharField(max_length=60, null=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('categoryID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colors', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabrics', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'home/')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mailinglist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occasions', models.CharField(max_length=60)),
            ],
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
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.ForeignKey(to='myapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Pastorders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('image', models.ImageField(upload_to=b'pattern/')),
                ('patternID', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('image', models.ImageField(null=True, upload_to=b'home/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('productID', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(default=b'none', max_length=300)),
                ('unitsInOrder', models.IntegerField(default=0)),
                ('unitsInStock', models.IntegerField(default=0)),
                ('views', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='myapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('SubCategoryID', models.IntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(to='myapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=30, null=True, blank=True)),
                ('length_blouse', models.IntegerField(null=True, blank=True)),
                ('waist_blouse', models.IntegerField(null=True, blank=True)),
                ('sleeve_length', models.IntegerField(null=True, blank=True)),
                ('neck_front', models.IntegerField(null=True, blank=True)),
                ('bust', models.IntegerField(null=True, blank=True)),
                ('shoulder', models.IntegerField(null=True, blank=True)),
                ('sleeve_width', models.IntegerField(null=True, blank=True)),
                ('neck_back', models.IntegerField(null=True, blank=True)),
                ('address_line1', models.CharField(max_length=100, null=True, blank=True)),
                ('address_line2', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('postcode', models.IntegerField(null=True, blank=True)),
                ('cardname', models.CharField(max_length=100, null=True, blank=True)),
                ('cardno', models.IntegerField(null=True, blank=True)),
                ('exp_month', models.CharField(max_length=50, null=True, blank=True)),
                ('exp_year', models.IntegerField(null=True, blank=True)),
                ('cvv', models.IntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wish_products', models.IntegerField()),
                ('user', models.ForeignKey(to='myapp.UserProfile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('works', models.CharField(max_length=60)),
                ('product', models.ManyToManyField(to='myapp.Product', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(to='myapp.SubCategory', null=True),
        ),
        migrations.AddField(
            model_name='pastorders',
            name='user',
            field=models.ForeignKey(to='myapp.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='productID',
            field=models.OneToOneField(to='myapp.Product'),
        ),
        migrations.AddField(
            model_name='occasion',
            name='product',
            field=models.ManyToManyField(to='myapp.Product', null=True),
        ),
        migrations.AddField(
            model_name='images',
            name='product',
            field=models.ForeignKey(to='myapp.Product', null=True),
        ),
        migrations.AddField(
            model_name='fabric',
            name='product',
            field=models.ManyToManyField(to='myapp.Product', null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ManyToManyField(to='myapp.Product', null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='myapp.UserProfile', null=True),
        ),
    ]
