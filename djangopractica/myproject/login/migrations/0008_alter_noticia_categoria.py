# Generated by Django 3.2.16 on 2022-12-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_noticia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.categoria'),
        ),
    ]
