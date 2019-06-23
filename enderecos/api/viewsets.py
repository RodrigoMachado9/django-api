from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
        """
    # todo > object = manager ,  view convesando com model
    # pegando tudo o que estiver no banco de dados e atribuindo a variavel > queryset

    queryset = Endereco.objects.all()
    # todo transformando os dados em json
    serializer_class = EnderecoSerializer
