# vim: set fileencoding=utf-8 :
"""
__init__ file of the pyramid application
Contain the main function
"""
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory

from pyramidapp.models import BASE, DB_SESSION
from pyramidapp.models.item import Item
from pyramidapp.models.security import ACL, groups_finder

from sqlalchemy import engine_from_config, event

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

    if settings['sqlalchemy.url'] in os.environ:
        engine = engine_from_config(settings, 'sqlalchemy.', url=os.environ[settings['sqlalchemy.url']])
    else:
        engine = engine_from_config(settings, 'sqlalchemy.')

    DB_SESSION.configure(bind=engine)

    factory_s = settings['pyramid.session_factory_secret']
    auth_s = settings['pyramid.authentication_secret']

    session_factory = SignedCookieSessionFactory(factory_s)
    auth_policy = AuthTktAuthenticationPolicy(auth_s, callback=groups_finder)

    config = Configurator(settings=settings,
                          authentication_policy=auth_policy,
                          root_factory=RootFactory)

    config.set_session_factory(session_factory)
    config.add_static_view(name='static', path='pyramidapp:static')

    config.add_route('home', '/')

    #Category routes
    config.add_route('view_category',
                     r'/category-{idItem:\d+}-{nameItem}/index.html')
    config.add_route('new_category', r'/new-category.html')
    config.add_route('new_sub_category',
                     r'/category-{idItem:\d+}-{nameItem}/%s' % (
                         'new-category.html'))
    config.add_route('edit_category',
                     r'/category-{idItem:\d+}-{nameItem}/%s' % (
                         'edit.html'))
    config.add_route('delete_category',
                     r'/category-{idItem:\d+}-{nameItem}/%s' % (
                         'delete.html'))

    config.add_route('view_picture',
                     r'/picture-{idItem:\d+}-{nameItem}/%s' % (
                         'index.html'))
    config.add_route('delete_picture',
                     r'/picture-{idItem:\d+}-{nameItem}/%s' % (
                         'delete.html'))
    config.add_route('new_picture',
                     r'/category-{idItem:\d+}-{nameItem}/%s' % (
                         'new-picture.html'))

    #Thumbnail route
    config.add_route('thumbnail', r'/thumbnail-{idItem:\d+}-{nameItem}')
    config.add_route('original_picture', r'/picture-{idItem:\d+}-{nameItem}')
    config.add_route('thumbnail_over',
                     r'/thumbnail-over-{idItem:\d+}-{nameItem}')





    #Admin routes
    config.add_route('home_admin', r'/admin/index.html')

    config.add_route('manage_comments', r'/admin/comment/list.html')
    config.add_route('validate_comment', r'/admin/comment/validate-{idComment:\d+}.html')
    config.add_route('delete_comment', r'/admin/comment/delete-{idComment:\d+}.html')

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
    config.begin()

    return config.make_wsgi_app()
