from django.db import models

from collector.data.DEPARTEMENTS import DEPARTEMENTS

class Inscrit(models.Model):

	# Rentré par l'utilisateur
	email = models.EmailField(max_length=255, unique=True)
	prenom = models.CharField("prénom", max_length=255, null=True)
	nom = models.CharField(max_length=255)
	numero_adherent = models.PositiveSmallIntegerField("numéro d'adhérent", max_length=10, blank=True, null=True)
	date_de_naissance = models.DateField()
	adresse_postale = models.CharField(max_length=512, blank=True, null=True)
	numero_de_telephone = models.PositiveSmallIntegerField("téléphone", max_length=12, blank=True, null=True)
	departement = models.CharField("département", max_length=3, choices=DEPARTEMENTS, null=True)
	compte_twitter = models.CharField(max_length=255, blank=True, null=True, default='@')
	compte_facebook = models.URLField(max_length=255, blank=True, null=True, default='http://facebook.com/')
	bio = models.TextField(max_length=512, blank=True, null=True)

	import os
	def get_upload_path(instance, filename):
		return os.path.join(
			instance.nom, "-", instance.prenom, filename)

	photo = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
	cni = models.FileField("Pièce d'identité", upload_to=get_upload_path, blank=True, null=True)
	declaration = models.FileField("Déclaration de candidature", upload_to=get_upload_path, blank=True, null=True)

	# Système
	created = models.DateTimeField(auto_now_add=True)
	code = models.PositiveSmallIntegerField(max_length=6)

	def __str__(self):
		return self.prenom + ' ' + self.nom

