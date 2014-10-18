from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *

class InscritAdmin(admin.ModelAdmin):
	model = Inscrit
	list_display = ("nom", "prenom")
	
admin.site.register(Inscrit, InscritAdmin)