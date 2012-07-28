from django.contrib import admin

from models import Chirp

class ChirpAdmin(admin.ModelAdmin):
	list_display = ['name', 'time', 'chirp']
	list_filter = ['name']

admin.site.register(Chirp, ChirpAdmin)
