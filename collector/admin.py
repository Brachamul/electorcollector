from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *

class InscritAdmin(admin.ModelAdmin):
	model = Inscrit
	list_display = ("nom", "prénom")
	
admin.site.register(Inscrit, InscritAdmin)