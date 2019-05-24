from common.db_connector import Base, engine, Session
from game_list.script.game import Game


def insert_game(gametitle, release, usadate, jpndate, eurdate, ausdate, usacart, jpncart, eurcart, auscart, english, notes):

    Base.metadata.create_all(engine)

    session = Session()

    game = Game(gametitle, release, usadate, jpndate, eurdate, ausdate, usacart, jpncart, eurcart, auscart, english, notes)
    session.add(game)
    session.commit()
    session.close()
