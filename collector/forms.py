from django import forms
from django.forms.extras.widgets import SelectDateWidget
from collector.data.MOIS import MOIS
# Forms !

from .models import *

class InscritForm(forms.ModelForm):
	class Meta:
		model = Inscrit
		fields = ['email', 'prénom', 'nom', 'date_de_naissance', 'département', 'compte_twitter', 'compte_facebook', 'photo', 'document']
		widgets = {
			'date_de_naissance': SelectDateWidget(months=MOIS, years=reversed(range(1900, 2000))),
		}

