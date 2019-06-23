from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
        """
    # todo > object = manager ,  view convesando com model
    # pegando tudo o que estiver no banco de dados e atribuindo a variavel > queryset

    queryset = Atracao.objects.all()
    # todo transformando os dados em json
    serializer_class = AtracaoSerializer
    filterset_fields = ('nome', 'descricao')

