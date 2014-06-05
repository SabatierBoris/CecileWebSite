from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello!')

def main(global_config, **settings):
    """
    This function returns a WSGI application.
    """

    config = Configurator(settings=settings)

    config.add_view(hello_world)

    return config.make_wsgi_app()
