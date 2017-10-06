from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.defaults import page_not_found
from .models import Chat
from .models import Document
from .forms import DocumentForm
from .forms import PostForm, CommentForm
from .models import Post, Comment

@login_required(login_url='/ingresar')
def post_list(request):
    posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required(login_url='/ingresar')
def post_list_alumnos(request):
    posts = Post.objects.all().filter(chismes_de="Alumno")
    return render(request, 'blog/alumnos.html', {'posts': posts})


@login_required(login_url='/ingresar')
def post_list_profesores(request):
    posts = Post.objects.all().filter(chismes_de="Profesor")
    return render(request, 'blog/profesores.html', {'posts': posts})

@login_required(login_url='/ingresar')
def post_list_otros(request):
    posts = Post.objects.all().filter(chismes_de="Otros")
    return render(request, 'blog/otros.html', {'posts': posts})


@login_required(login_url='/ingresar')
def archivos_otros(request):
    documents = Document.objects.all().filter(chismes_de="Otros")
    return render(request, 'blog/archivos_otros.html', {'documents': documents})

@login_required(login_url='/ingresar')
def archivos_alumnos(request):
    documents = Document.objects.all().filter(chismes_de="Alumno")
    return render(request, 'blog/archivos_alumnos.html', {'documents': documents})


@login_required(login_url='/ingresar')
def archivos_profesores(request):
    documents = Document.objects.all().filter(chismes_de="Profesor")
    return render(request, 'blog/archivos_profesores.html', {'documents': documents})



@login_required(login_url='/ingresar')
def post_list_privado(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list_privado.html', {'posts': posts})


@login_required(login_url='/ingresar')
def privado_archivos(request):
    archivos = Document.objects.filter(author=request.user)
    return render(request, 'blog/privado_archivos.html', {'archivos': archivos})

@login_required(login_url='/ingresar')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required(login_url='/ingresar')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listado')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required(login_url='/ingresar')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('listado')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required (login_url='/ingresar')
def privado (request):
    usuario = request.user
    return render_to_response('blog/privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar (request):
    logout (request)
    return HttpResponseRedirect('/')

def post_detail_privado(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail_privado.html', {'post': post})





def nuevo_usuario(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('blog/nuevousuario.html', {'form': form}, context_instance=RequestContext(request))


def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso) 
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('blog/ingresar/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('blog/nousuario.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('blog/ingresar.html', {'form': form}, context_instance=RequestContext(request))






@login_required (login_url='/ingresar')
def Chat_grupal(request):
    c = Chat.objects.all()
    return render(request, "blog/chat.html", {'home': 'active', 'chat': c})


@login_required (login_url='/ingresar')
def Mensaje(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')


@login_required (login_url='/ingresar')
def Messages(request):
    c = Chat.objects.all()
    username = request.POST['username']
    return render(request, 'blog/messages.html', {'chat': c})


@login_required (login_url='/ingresar')
def post_document(request):
    documents = Document.objects.all()
    return render(request, 'blog/post_document.html', { 'documents': documents })


@login_required (login_url='/ingresar')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_document')
    else:
        form = DocumentForm()
    return render(request, 'blog/model_form_upload.html', {
        'form': form
    })


@login_required (login_url='/ingresar')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

