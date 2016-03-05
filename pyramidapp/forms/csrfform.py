# vim: set fileencoding=utf-8 :
"""
Form securised with a CSRF
"""

from wtforms.ext.csrf import SecureForm


class CSRFSecureForm(SecureForm):
    """
    Base form class supporting CSRF
    """
    def __init__(self, *a, **kw):
        self.request = kw.pop('request')
        super().__init__(*a, **kw)

    def generate_csrf_token(self, csrf_context):
        return self.request.session.get_csrf_token()

    def validate_csrf_token(self, field):
        if field.data != field.current_token:
            raise ValueError('Invalide CSRF')
