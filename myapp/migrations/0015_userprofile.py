# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0014_auto_20150407_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('length_blouse', models.IntegerField(null=True, blank=True)),
                ('waist_blouse', models.IntegerField(null=True, blank=True)),
                ('sleeve_length', models.IntegerField(null=True, blank=True)),
                ('neck_front', models.IntegerField(null=True, blank=True)),
                ('bust', models.IntegerField(null=True, blank=True)),
                ('shoulder', models.IntegerField(null=True, blank=True)),
                ('sleeve_width', models.IntegerField(null=True, blank=True)),
                ('neck_back', models.IntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
