# vim: set fileencoding=utf-8 :
"""
The comment view part
"""
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from sqlalchemy.exc import IntegrityError

from pyramidapp.models.tag import Tag
from pyramidapp.models.menu import MenuAdministration
from pyramidapp.models.comment import Comment



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
        comment_list = Comment.get_waiting_for_validation()
        return {'tags' : Tag.all(),
                'contents': comment_list}

    @view_config(route_name='validate_comment',
                 permission='comment')
    def comment_validate(self):
        idcomment = int(self.request.matchdict.get('idComment', -1))
        comment = Comment.by_uid(idcomment)

        session = Comment.get_session()
        comment.valid = True
        session.commit()

        url = self.request.route_url('manage_comments')
        return HTTPFound(url)

    @view_config(route_name='delete_comment',
                 permission='comment')
    def comment_delete(self):
        idcomment = int(self.request.matchdict.get('idComment', -1))
        comment = Comment.by_uid(idcomment)

        session = Comment.get_session()
        session.delete(comment)
        session.commit()

        url = self.request.route_url('manage_comments')
        return HTTPFound(url)
