from django.db import models
from datetime import date

# Create your models here.


class ejemplo(models.Model):
    name = models.CharField(max_length=50)


class Categoria(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='images/', blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE)
    fecha_pub = models.DateField(default=date.today)
    #numero_comentarios = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo + ' - ' + self.categoria.name


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    noticia = models.ForeignKey(
        Noticia, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.noticia.titulo + " - " + self.nombre
