# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscrit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('naissance', models.DateField()),
                ('departement', models.PositiveSmallIntegerField(max_length=3)),
                ('twitter', models.CharField(null=True, blank=True, max_length=255)),
                ('facebook', models.URLField(null=True, blank=True, max_length=255)),
                ('photo', models.ImageField(null=True, blank=True, upload_to='photos')),
                ('document', models.FileField(null=True, blank=True, upload_to='documents')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.PositiveSmallIntegerField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
