from django.contrib import admin
from .models import(Persona)
from .models import(Empresa)
from .models import(OfertaDeTrabajo)
from .models import(APC)
# Register your models here.

admin.site.register(Persona)
admin.site.register(Empresa)
admin.site.register(OfertaDeTrabajo)
admin.site.register(APC)
