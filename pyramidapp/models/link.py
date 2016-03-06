# vim: set fileencoding=utf-8 :
"""
Link Model module
"""
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from . import (
    Dateable,
    BASE,
)


class Link(Dateable, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Link Model
    """
    __tablename__ = 'link'
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})
    link = Column(String,
                  nullable=False,
                  info={'trim': True})

    item_id = Column(Integer, ForeignKey('item.uid'))
    item = relationship("Item", back_populates="link")

    def __init__(self, name="", link=""):
        super().__init__()
        self.name = name
        self.link = link
