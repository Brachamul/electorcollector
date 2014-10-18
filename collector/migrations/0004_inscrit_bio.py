# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0003_auto_20141009_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='bio',
            field=models.TextField(max_length=1024, blank=True, null=True),
            preserve_default=True,
        ),
    ]
