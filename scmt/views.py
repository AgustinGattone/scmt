from django.shortcuts import render

# Create your views here.

def persona_list(request):
    return render(request, 'scmt/persona_list.html', {})

