from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def landing(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def playground(request):
    return render(request, 'playground.html')


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
    return render(request, 'posts.html', {
        'noticias': noticias,
    })


# def crearPost(request):
    # if request.method == 'POST':
    #post_form = CrearNoticia(request.POST or None, request.FILES or None)
    # if post_form.is_valid():
    # post_form.save()
    # return redirect('posts')
    # else:
    #post_form = CrearNoticia()
    # return render(request, 'blog.html', {'post_form': post_form})
