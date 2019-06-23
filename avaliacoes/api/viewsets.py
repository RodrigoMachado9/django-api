from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
        """
    # todo > object = manager ,  view convesando com model
    # pegando tudo o que estiver no banco de dados e atribuindo a variavel > queryset

    queryset = Avaliacao.objects.all()
    # todo transformando os dados em json
    serializer_class = AvaliacaoSerializer
