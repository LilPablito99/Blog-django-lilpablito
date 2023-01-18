from django.contrib import admin
from .models import Usuario, Post, Comentario,Categoria

admin.site.register([Usuario, Post, Comentario, Categoria])
