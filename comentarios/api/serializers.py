
from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        #todo warning cuidado com os espaços ao criar os atributos -  Hehe
        fields = ('id','usuario', 'comentario', 'data',
                  'aprovado')
