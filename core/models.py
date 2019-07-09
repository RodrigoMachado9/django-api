from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

# Create your models here.
class PontoTuristico(models.Model):
    #todo  determinados campos da minha classe model

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    #todo relacionamento com a tabela/classe Atracao, package: atracoes...
    atracoes  = models.ManyToManyField(Atracao)

    #todo relacionamento com a tabela/classe Comentario, package: comentarios...
    comentarios  = models.ManyToManyField(Comentario)

    # todo relacionamento com a tabela/classe Avaliacao, package: avaliacoes...
    avaliacoes  = models.ManyToManyField(Avaliacao)

    #todo relacionamento com a tabela endereço
    endereco =  models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)

    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    #todo serializer ->                      fields [utilizando a property consigo acessar todos os atributos o objeto]
    #todo construir queryset para acesso ao banco de dados.

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)


    def __str__(self):
        return self.nome

    #todo model ou manager -> contem as regras de negocios = verificar metodos constante no arquivo serializer e passar para ca.
