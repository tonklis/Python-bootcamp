# Create your views here.

from models import Chirp
from django.shortcuts import render_to_response

#def index(request):
#	return HttpResponseNotFound()

def chirp_list(request):
	chirps = Chirp.objects.all().order_by("time")
	#chirps.filter(name="Dough...").count()
	#Chirp.objects.get(pk=1)
	#Chirp.objects.filter(pk__in=[1,2,3,4,5])
	#Chirp.objects.filter(time__gte=datetime.now() - datetime(days=20))
	#Chirp.objects.get(name="Doug"")
	return render_to_response('chirp_base.haml', {'chirps' : chirps})
