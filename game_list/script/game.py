from sqlalchemy import Column, String, Integer, Boolean

from common.db_connector import Base


class Game(Base):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    gametitle = Column(String)
    release = Column(String)
    usadate = Column(String)
    jpndate = Column(String)
    eurdate = Column(String)
    ausdate = Column(String)
    usacart = Column(String)
    jpncart = Column(String)
    eurcart = Column(String)
    auscart = Column(String)
    english = Column(Boolean)
    notes = Column(String)

    def __init__(
            self, gametitle, release=None, usadate=None, jpndate=None, eurdate=None, ausdate=None,
            usacart=None, jpncart=None, eurcart=None, auscart=None, english=None, notes=None
    ):
        self.gametitle = gametitle
        self.release = release
        self.usadate = usadate
        self.jpndate = jpndate
        self.eurdate = eurdate
        self.ausdate = ausdate
        self.usacart = usacart
        self.jpncart = jpncart
        self.eurcart = eurcart
        self.auscart = auscart
        self.english = english
        self.notes = notes

