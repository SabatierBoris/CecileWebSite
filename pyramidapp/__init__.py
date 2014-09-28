# coding : utf-8
"""
__init__ file of the pyramid application
Contain the main function
"""
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory

from sqlalchemy import engine_from_config

from .models import DB_SESSION, BASE


def hello_world(request):
    """
    Example of a request function
    """
    request = request  # Remove W0613
    return Response('Hello!')


def main(global_config, **settings):
    """
    This function returns a WSGI application.
    """
    global_config = global_config  # Remove W0613

    engine = engine_from_config(settings, 'sqlalchemy.')
    DB_SESSION.configure(bind=engine)

    session_factory = SignedCookieSessionFactory('itsaseekreet')

    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.set_session_factory(session_factory)
    config.add_static_view(name='static', path='pyramidapp:static')

    config.add_route('home', '/')
    # Administration route
    config.add_route('right_list', r'/admin/right')
    config.add_route('right_list:new', r'/admin/right/{new}')
    config.add_route('right_delete', r'/admin/right/{uid:\d+}/delete')

    config.add_route('group_list', r'/admin/group')
    config.add_route('group_list:new', r'/admin/group/{new}')
    config.add_route('group_delete', r'/admin/group/{uid:\d+}/delete')

    config.add_route('user_list', r'/admin/user')
    config.add_route('user_list:new', r'/admin/user/{new}')

    config.scan()

    return config.make_wsgi_app()
