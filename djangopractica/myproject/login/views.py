from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.


def landing(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def create_post(request):
    if request.method == 'GET':
        return render(request, 'blog.html', {
            'form': crearNoticia
        })
    else:
        Noticia.objects.create(
            titulo=request.POST['titulo'],
            contenido=request.POST['contenido'],
            categoria_id=1,
            imagen=request.FILES.get('imagen', None))
        return redirect('/posts/')


def posts(request):
    noticias = Noticia.objects.all()
    comentarios = Comentario.objects.all()
    return render(request, 'posts.html', {
        'noticias': noticias,
        'comentarios': comentarios,
    })


# def addComentario(CreateView):
    #model = Comentario
    #template_name = 'comentar.html'
    #fields = '_all_'
