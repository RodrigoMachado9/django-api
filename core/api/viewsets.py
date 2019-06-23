from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    #todo > object = manager ,  view convesando com model
    # pegando tudo o que estiver no banco de dados e atribuindo a variavel > queryset

    #queryset = PontoTuristico.objects.all()
    # todo transformando os dados em json
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    #todo pesquisa case insensitive   > estudar documentaçaõ filters ->  o simbolo(istartswith):  ^ retornará determinado valor que contenha pelo menos o seu inicio na busca.
    search_fields = ('nome', 'descricao', 'endereco__linha1', '^endereco__linha2')


    """ 
        a funcionalidade > lookup_field -> permite que o django realize buscas utilizando o nome referente 
        a determinado atributo, entretanto o mesmo deverá ser unique 
    """
    #lookup_field = 'nome'


    #todo por default aprovado  = False,  logo sera necessário definir via browser, aprovado=True
    def get_queryset(self):
        #return PontoTuristico.objects.filter(aprovado=True)
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
            #todo __iexact  -> permite o case insensitive

        return queryset



    #todo metodo > sobreescreve o metodo list
    def list(self, request, *args, **kwargs):
        #return Response({'teste':123})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    #todo > Debugger
    def create(self, request, *args, **kwargs):
        #return Response({'Hello!': request.data['nome']})
        return super(PontoTuristicoViewSet,  self).create(request, *args, **kwargs)



    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    #todo retorna um objeto, fazer validações.  gerar logs.
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)




    #@action(methods=['get'], detail=True)
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass


    #todo se a necessidade de utilizar a PK
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass