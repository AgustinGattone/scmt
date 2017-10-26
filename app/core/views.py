from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from app.core.forms import RegistroDesocupado, RegistroEmpresa, RegistroOfertaDeTrabajo
from app.core.models import *

@login_required
def home(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'home.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})
    #def get_absolute_url(self):
        #return reverse('author-detail', kwargs={'pk': self.pk})


def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})

def registro_ofertaDeTrabajo(request):
    if request.method == "GET":
        return get_registro_ofertaDeTrabajo_form(request)
    elif request.method == 'POST':
        return handle_registro_ofertaDeTrabajo_form(request)

def get_registro_ofertaDeTrabajo_form(request):
    form = RegistroOfertaDeTrabajo()
    return render(request, 'crear_oferta.html', {'form': form})

def handle_registro_ofertaDeTrabajo_form(request):
    form = RegistroOfertaDeTrabajo(request.POST)
    if form.is_valid():
        return redirect('home')
    else:
        form=RegistroOfertaDeTrabajo()
        return render(request, 'crear_oferta.html', {'form': form})

  def user_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = RegistroDesocupado(request.user, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                user.username = request.user
                post.save()
                return redirect('user_edit', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'user_edit.html', {'form': form})


class EliminarDesocupado(DeleteView):
    model = Desocupado
    success_url = reverse_lazy('user')
