# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscrit',
            old_name='facebook',
            new_name='compte_facebook',
        ),
        migrations.RenameField(
            model_name='inscrit',
            old_name='twitter',
            new_name='compte_twitter',
        ),
        migrations.RenameField(
            model_name='inscrit',
            old_name='naissance',
            new_name='date_de_naissance',
        ),
        migrations.RenameField(
            model_name='inscrit',
            old_name='departement',
            new_name='département',
        ),
        migrations.RenameField(
            model_name='inscrit',
            old_name='prenom',
            new_name='prénom',
        ),
    ]
