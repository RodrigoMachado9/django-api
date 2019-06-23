from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        #todo warning cuidado com os espaços ao criar os atributos -  Hehe
        fields = ('id','user', 'comentario', 'nota',
                  'data')
