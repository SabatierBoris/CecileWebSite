# vim: set fileencoding=utf-8 :
"""
Tags Field forms
"""
from wtforms.fields import (
    Field
)
from wtforms.widgets import (
    TextInput
)


class TagListField(Field):
    """
    Tags field class
    """
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = list(self._remove_duplicates([x.strip() for x in valuelist[0].split(',')]))
        else:
            self.data = []

    @classmethod
    def _remove_duplicates(cls, seq):
        """
        Remove duplicates in a case insensitive, but case preserving manner
        """
        d = {}
        for item in seq:
            data = item.strip().lower()
            if len(data) > 0 and data not in d:
                d[data] = True
                yield data
