# vim: set fileencoding=utf-8 :
"""
The comment view part
"""
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.group import Group, GroupRightAccess
from pyramidapp.models.right import Right

from pyramidapp.forms.group import GroupForm


class CommentView(object):
    """
    The comment view logic
    """
    def __init__(self, request):
        self.request = request

    @MenuAdministration(order=6,
                        display='Validation des commentaires',
                        route_name="manage_comments")
    @view_config(route_name='manage_comments',
                 renderer='admin/comment.mak',
                 permission='comment')
    def comment_list(self):
        pass
