from django import forms
from django.forms.extras.widgets import SelectDateWidget
from collector.data.MOIS import MOIS
# Forms !

from .models import *

import datetime

class InscritForm(forms.ModelForm):
	class Meta:
		model = Inscrit
		fields = ['email', 'prenom', 'nom', 'adresse_postale', 'numero_de_telephone', 'numero_adherent', 'date_de_naissance', 'photo', 'bio', 'departement', 'compte_twitter', 'compte_facebook']
		# , 'document'
		help_texts = {
			'photo': 'Cette photo sera utilisée pour vous représenter dans nos supports de communication.',
			'bio': 'Un court texte de présentation pour accompagner la photo, 500 caractères maxi.',
			'numero_adherent': 'Si vous le connaissez...',
			'adresse_postale': 'Numéro, rue, code postal, ville, ...'
		}
		widgets = {
			'date_de_naissance': SelectDateWidget(months=MOIS, years=range(2000, 1930, -1)),
		}