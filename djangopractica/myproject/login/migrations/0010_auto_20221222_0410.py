# Generated by Django 3.2.16 on 2022-12-22 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='noticia',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='numero_comentarios',
        ),
    ]
