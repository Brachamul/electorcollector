# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import collector.models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0007_auto_20141024_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscrit',
            name='document',
        ),
        migrations.AddField(
            model_name='inscrit',
            name='cni',
            field=models.FileField(upload_to=collector.models.Inscrit.get_upload_path, null=True, blank=True, verbose_name="Pièce d'identité"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscrit',
            name='declaration',
            field=models.FileField(upload_to=collector.models.Inscrit.get_upload_path, null=True, blank=True, verbose_name='Déclaration de candidature'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='departement',
            field=models.CharField(choices=[('75', '75 - Paris'), ('77', '77 - Seine-et-Marne'), ('78', '78 - Yvelines'), ('91', '91 - Essonne'), ('92', '92 - Hauts-de-Seine'), ('93', '93 - Seine-Saint-Denis'), ('94', '94 - Val-de-Marne'), ('95', "95 - Val-d'Oise")], max_length=3, null=True, verbose_name='département'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='photo',
            field=models.ImageField(upload_to=collector.models.Inscrit.get_upload_path, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='prenom',
            field=models.CharField(max_length=255, null=True, verbose_name='prénom'),
        ),
    ]
