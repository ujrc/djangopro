# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 16:33
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
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True)),
                ('album_logo', models.FileField(blank=True, max_length=25, upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.FileField(choices=[('wav', 'wav'), ('mp3', 'mp3'), ('ogg', 'ogg')], upload_to='')),
                ('song_title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=25)),
                ('is_favorite', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.Album')),
            ],
        ),
    ]
