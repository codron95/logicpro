# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-18 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20160716_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='associates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('desig', models.CharField(default='', max_length=40)),
                ('logo', models.ImageField(default=0, upload_to='assocs/')),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(default=0, upload_to='clients/'),
        ),
    ]
