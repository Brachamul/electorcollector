# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_auto_20141018_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='adresse_postale',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscrit',
            name='numéro_de_téléphone',
            field=models.PositiveSmallIntegerField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
    ]
