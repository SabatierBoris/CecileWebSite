# vim: set fileencoding=utf-8 :
"""
Right Model module
"""
from sqlalchemy import (
    Column,
    String,
)

from . import (
    Dateable,
    BASE,
)


class Right(Dateable, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Right Model
    """
    __tablename__ = 'right'
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})

    def __init__(self, name=""):
        super().__init__()
        self.name = name
