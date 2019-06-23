from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        #todo warning cuidado com os espaços ao criar os atributos -  Hehe
        fields = ('id','linha1', 'linha2', 'cidade',
                  'estado','pais', 'latitude', 'logitude')
