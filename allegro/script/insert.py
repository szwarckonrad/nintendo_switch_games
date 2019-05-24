from common.db_connector import Base, engine, Session
from .offer import Offer


def insert_offer(allegro_id, date, name, sold_by_company, available_for_free_delivery,
                 price, lowest_delivery_cost, allegro_seller_id, price_currency, delivery_cost_currency,
                 allegro_category):

    Base.metadata.create_all(engine)

    session = Session()

    offer = Offer(allegro_id, date, name, sold_by_company, available_for_free_delivery,
                  price, lowest_delivery_cost, allegro_seller_id, price_currency, delivery_cost_currency,
                  allegro_category)

    session.add(offer)
    session.commit()
    session.close()
