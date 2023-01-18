# Generated by Django 4.1.5 on 2023-01-18 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='date published')),
                ('contenido', models.TextField()),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.categorias')),
                ('usuarios_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.posts')),
                ('usuarios_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.usuarios')),
            ],
        ),
    ]