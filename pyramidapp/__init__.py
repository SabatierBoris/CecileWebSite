# vim: set fileencoding=utf-8 :
"""
__init__ file of the pyramid application
Contain the main function
"""
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory

from sqlalchemy import engine_from_config, event

from .models import DB_SESSION, BASE
from .models.security import groups_finder
from .models.security import ACL
from pyramidapp.models.item import Item
import os


class RootFactory(object):
    # pylint: disable=R0903
    """
    RootFactory for ACL setting
    """
    __acl__ = ACL()

    def __init__(self, request):
        pass


def main(global_config, **settings):
    """
    This function returns a WSGI application.
    """
    global_config = global_config  # Remove W0613

    engine = engine_from_config(settings, 'sqlalchemy.')

    # pylint: disable=W0612
    @event.listens_for(engine, "connect")
    def do_connect(dbapi_connection, connection_record):
        """
        This function set isolation_level to None
        if use a sqlite database for be able to
        use nested_session
        """
        connection_record = connection_record
        if engine.dialect.name == "sqlite":
            dbapi_connection.isolation_level = None

    DB_SESSION.configure(bind=engine)

    factory_s = settings['pyramid.session_factory_secret']
    auth_s = settings['pyramid.authentication_secret']

    session_factory = SignedCookieSessionFactory(factory_s)
    auth_policy = AuthTktAuthenticationPolicy(auth_s, callback=groups_finder)

    config = Configurator(settings=settings,
                          authentication_policy=auth_policy,
                          root_factory=RootFactory)
    config.include('pyramid_mako')
    config.set_session_factory(session_factory)
    config.add_static_view(name='static', path='pyramidapp:static')

    config.add_route('home', '/')

    config.add_route('view_category',
                     r'/category-{idCategory:\d+}-{nameCategory}/index.html')
    config.add_route('new_category', r'/new-category.html')
    config.add_route('new_sub_category',
                     r'/category-{idCategory:\d+}-{nameCategory}/%s' % (
                         'new-category.html'))
    config.add_route('thumbnail', r'/thumbnail-{idItem:\d+}-{nameItem}')
    config.add_route('thumbnail_over',
                     r'/thumbnail-over-{idItem:\d+}-{nameItem}')
    # Administration route
    config.add_route('home_admin', r'/admin/index.html')

    config.add_route('right_list', r'/admin/right/list.html')
    config.add_route('right_list:new', r'/admin/right/list-{new}.html')
    config.add_route('right_delete', r'/admin/right/delete-{uid:\d+}.html')

    config.add_route('group_list', r'/admin/group/list.html')
    config.add_route('group_list:new', r'/admin/group/list-{new}.html')
    config.add_route('group_delete', r'/admin/group/delete-{uid:\d+}.html')

    config.add_route('user_list', r'/admin/user/list.html')
    config.add_route('user_list:new', r'/admin/user/list-{new}.html')
    config.add_route('user_delete', r'/admin/user/delete-{uid:\d+}.html')

    config.add_route('login', r'/login.html')
    config.add_route('logout', r'/logout.html')

    config.scan()

    # Thumbnail remove
    for item in Item.all():
        if os.path.isfile(item.thumbnail):
            os.remove(item.thumbnail)
        if os.path.isfile(item.thumbnailover):
            os.remove(item.thumbnailover)

    return config.make_wsgi_app()
