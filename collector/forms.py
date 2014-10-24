from django import forms
from django.forms.extras.widgets import SelectDateWidget
from collector.data.MOIS import MOIS
# Forms !

from .models import *

import datetime

class InscritForm(forms.ModelForm):
	class Meta:
		model = Inscrit
		fields = ['email', 'prenom', 'nom', 'adresse_postale', 'numero_de_telephone', 'numero_adherent', 'date_de_naissance', 'bio', 'photo', 'cni', 'declaration', 'departement', 'compte_twitter', 'compte_facebook']
		# , 'document'
		help_texts = {
			'photo': 'Cette photo sera utilisée pour vous représenter dans nos supports de communication.',
			'bio': 'Un court texte de présentation pour accompagner la photo, 500 caractères maxi. Pensez à indiquer pourquoi vous êtes engagé au MoDem, vos responsabilités éventuelles, ainsi que les raisons de votre soutien à Fibre Démocrate.',
			'numero_adherent': 'Si vous le connaissez...',
			'adresse_postale': 'Numéro, rue, code postal, ville, ...',
			'declaration': 'Vous trouverez une déclaration type <a href="http://goo.gl/NIowBb" target="_blank">ici</a>.'
		}
		widgets = {
			'date_de_naissance': SelectDateWidget(months=MOIS, years=range(2000, 1930, -1)),
		}