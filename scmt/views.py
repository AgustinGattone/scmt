from django.shortcuts import render
from .models import Persona

# Create your views here.

def persona_list(request):
	persona = Persona.objects.all
	return render(request, 'scmt/persona_list.html', {'personas': persona})

