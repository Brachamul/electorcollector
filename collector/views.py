from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.

from .models import *
from .forms import *

class InscritView(FormView):
    template_name = 'form.html'
    form_class = InscritForm
    success_url = '/reussite/'

    def form_valid(self, form):
        form.instance.code = random.randint(100000, 999999) # un nombre à 6 chiffres
        return super(InscritView, self).form_valid(form)