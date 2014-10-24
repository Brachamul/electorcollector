# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_auto_20141018_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscrit',
            name='département',
        ),
        migrations.RemoveField(
            model_name='inscrit',
            name='numéro_adhérent',
        ),
        migrations.RemoveField(
            model_name='inscrit',
            name='numéro_de_téléphone',
        ),
        migrations.RemoveField(
            model_name='inscrit',
            name='prénom',
        ),
        migrations.AddField(
            model_name='inscrit',
            name='departement',
            field=models.CharField(default=0, verbose_name='département', choices=[('75', '75 - Paris'), ('77', '77 - Seine-et-Marne'), ('78', '78 - Yvelines'), ('91', '91 - Essonne'), ('92', '92 - Hauts-de-Seine'), ('93', '93 - Seine-Saint-Denis'), ('94', '94 - Val-de-Marne'), ('95', "95 - Val-d'Oise")], max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscrit',
            name='numero_adherent',
            field=models.PositiveSmallIntegerField(blank=True, max_length=10, verbose_name="numéro d'adhérent", null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscrit',
            name='numero_de_telephone',
            field=models.PositiveSmallIntegerField(blank=True, max_length=12, verbose_name='téléphone', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscrit',
            name='prenom',
            field=models.CharField(default=0, verbose_name='prénom', max_length=255),
            preserve_default=False,
        ),
    ]
