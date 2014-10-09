from django.db import models

from collector.data.DEPARTEMENTS import DEPARTEMENTS

class Inscrit(models.Model):

	# Rentré par l'utilisateur
	email = models.EmailField(max_length=255, unique=True)
	prénom = models.CharField(max_length=255)
	nom = models.CharField(max_length=255)
	date_de_naissance = models.DateField()
	département = models.CharField(max_length=3, choices=DEPARTEMENTS)
	compte_twitter = models.CharField(max_length=255, blank=True, null=True, default='@')
	compte_facebook = models.URLField(max_length=255, blank=True, null=True, default='http://facebook.com/')
	photo = models.ImageField(upload_to='photos', blank=True, null=True)
	document = models.FileField(upload_to='documents', blank=True, null=True)

	# Système
	created = models.DateTimeField(auto_now_add=True)
	code = models.PositiveSmallIntegerField(max_length=6)

	def __str__(self):
		return self.prénom + ' ' + self.nom