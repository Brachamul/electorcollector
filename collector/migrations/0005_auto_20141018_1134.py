# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_inscrit_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='numéro_adhérent',
            field=models.PositiveSmallIntegerField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='bio',
            field=models.TextField(max_length=512, null=True, blank=True),
        ),
    ]
