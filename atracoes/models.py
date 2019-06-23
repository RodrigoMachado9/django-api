from django.db import models

# Create your models here.

class Atracao(models.Model):
#todo atributos referente a class atracoes

    nome = models.CharField(max_length=150)
    descricao  =  models.TextField()
    horario_func =  models.TextField()
    idade_minima =  models.IntegerField()
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)


    def __str__(self):
        return self.nome
