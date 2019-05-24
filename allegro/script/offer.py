from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP

from common.db_connector import Base


class Offer(Base):

    __tablename__ = "offers"

    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP)
    allegro_id = Column(String)
    name = Column(String)
    price = Column(String)
    price_currency = Column(String)
    allegro_category = Column(String)
    lowest_delivery_cost = Column(String)
    delivery_cost_currency = Column(String)
    allegro_seller_id = Column(String)
    sold_by_company = Column(Boolean)
    available_for_free_delivery = Column(Boolean)

    def __init__(
            self, allegro_id, date, name, sold_by_company, available_for_free_delivery,
            price, lowest_delivery_cost, allegro_seller_id, price_currency, delivery_cost_currency, allegro_category
    ):
        self.date = date
        self.allegro_id = allegro_id
        self.name = name
        self.sold_by_company = sold_by_company
        self.available_for_free_delivery = available_for_free_delivery
        self.price = price
        self.lowest_delivery_cost = lowest_delivery_cost
        self.allegro_seller_id = allegro_seller_id
        self.price_currency = price_currency
        self.delivery_cost_currency = delivery_cost_currency
        self.allegro_category = allegro_category
