from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Comentario(models.Model):
    #todo essa aplicação ira herdar do django (users) | usuario pode realizar comentarios
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    #todo pega automaticamente a data do servidor apos o cadastro
    data = models.DateTimeField(auto_now_add=True)
    #todo status
    aprovado =  models.BooleanField(default=True)


    def __str__(self):
        return self.usuario.username

