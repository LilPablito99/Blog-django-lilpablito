from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=40)
    email = models.EmailField(max_length=254,unique=True)

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateTimeField('date published')
    contenido = models.TextField()
    usuarios_id = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)   

class Comentario(models.Model):
    comentario = models.TextField()
    usuarios_id = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
