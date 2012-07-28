from django.db import models

class Chirp(models.Model):
	name = models.CharField(default="Doug Graves!", max_length=30)
	time = models.DateTimeField()
	chirp = models.CharField(default="", max_length=140)
