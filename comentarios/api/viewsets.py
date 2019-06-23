from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    """
        A simple ViewSet for viewing and editing accounts.
        """
    # todo > object = manager ,  view convesando com model
    # pegando tudo o que estiver no banco de dados e atribuindo a variavel > queryset

    queryset = Comentario.objects.all()
    # todo transformando os dados em json
    serializer_class = ComentarioSerializer
