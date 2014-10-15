from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, UpdateView
from django.core.mail import send_mail
# Create your views here.

from .models import *
from .forms import *

class InscritView(FormView):
	template_name = 'form.html'
	form_class = InscritForm
	success_url = '/reussite/'

	def form_valid(self, form):
		import random
		code = random.randint(100000, 999999) # un nombre à 6 chiffres
		form.instance.code = code
		form.save()
		send_mail(
			'Votre inscription à la liste Fibre Démocrate',
			'Votre inscription a bien été prise en compte.\n\nCliquez sur le lien suivant pour la modifier:\n%s/%s&%s\n \nL\'équipe Fibre Démocrate'
			% ("antoningrele.pythonanywhere.com/modifier", form.instance.email, form.instance.code),
			'antonin.grele@gmail.com',
			['%s' % (form.instance.email)], fail_silently=False)
		return super(InscritView, self).form_valid(form)

def inscription_reussie(request):
	return render_to_response('form-success.html')


class ModifyView(UpdateView):
	template_name = 'form.html'
	form_class = InscritForm
	success_url = '/reussite/'

	def get_object(self):
		inscrit = Inscrit.objects.get(email=self.kwargs['email'], code=self.kwargs['code'])
	#   Nous n'avons pas trouvé votre inscription. N'hésitez pas à vous réinscrire, au pire.
		return inscrit