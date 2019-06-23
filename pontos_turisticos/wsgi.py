"""
WSGI config for pontos_turisticos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pontos_turisticos.settings')

#todo envolvendo > get_wsgi_application, usando o Cling > avalia se a requisição se trata de um arquivo statico ou não.

application = Cling(get_wsgi_application())


