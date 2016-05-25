# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=2)),
                ('stripe_id', models.CharField(blank=True, max_length=30)),
                ('user_sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'subscribers',
            },
        ),
    ]
