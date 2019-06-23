from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    #todo reuso de codigo, atributos.
    endereco = EnderecoSerializer()

    #todo incrementando o meu serializer: com MethodField > adicionando um atributo novo.
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        #todo warning cuidado com os espaços ao criar os atributos -  Hehe
        fields = ('id', 'nome', 'descricao','aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa','descricao_completa2'
                  )

    #todo descricao_completa2 -> classe modelo hehe

    #todo o retorno serão os atributos concatenados .
    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)