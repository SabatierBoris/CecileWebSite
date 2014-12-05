# vim: set fileencoding=utf-8 :
"""
Security module
"""

from pyramid.security import Allow

from pyramidapp.models.user import User
from pyramidapp.models.group import Group


def groups_finder(login, request):
    """
    Function to know the groups of a user
    Used by security module of pyramid
    """
    # Has 3 potential returns:
    #     - None, meaning userid doesn't exist
    #     - An empty list, meaning existing user but no group
    #     - List of groups for that userid
    user = User.by_login(login)
    request = request
    if user is None:
        return
    for group in user.groups:
        yield group.name


class ACL(object):
    # pylint: disable=R0903
    """
    Class list like for ACL access managed with BDD
    """
    def __len__(self):
        """
        Get the number of ACL
        """
        size = 0
        for group in Group.all():
            size += len(group.rights)
        return size

    def __getitem__(self, key):
        """
        Get the ACL number @key
        """
        i = 0
        for val in self:
            if i == key:
                return val
            i += 1

    def __iter__(self):
        """
        Get a iterator of ACL
        """
        for group in Group.all():
            for right in group.rights:
                yield(Allow, group.name, right.name)
