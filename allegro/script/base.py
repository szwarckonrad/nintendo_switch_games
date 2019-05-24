import os
import sys
from datetime import datetime

from allegro.script.constants import OFFER_BATCH
from allegro.script.fetch import fetch_allegro_token, fetch_offer_count, fetch_offer_list
from allegro.script.insert import insert_offer


def main():
    try:
        allegro_auth_string = os.environ["ALLEGRO_AUTH_STRING"]
    except KeyError as err:
        print(f"No allegro auth string provided. ERROR: {err}")
        sys.exit()

    allegro_token = fetch_allegro_token(allegro_auth_string)

    current_offer = 0
    offer_count = fetch_offer_count(allegro_token)

    while current_offer < offer_count:
        print(f"Fetching offers {current_offer} to {current_offer + OFFER_BATCH} out of all {offer_count}")
        offer_batch = fetch_offer_list(allegro_token, current_offer)
        promoted = offer_batch["items"]["promoted"]
        regular = offer_batch["items"]["regular"]

        offers = promoted + regular

        for offer in offers:
            allegro_id = offer["id"]
            date = datetime.utcnow()
            name = offer["name"]
            sold_by_company = offer["seller"]["company"]
            available_for_free_delivery = offer["delivery"]["availableForFree"]
            price = offer["sellingMode"]["price"]["amount"]
            lowest_delivery_cost = offer["delivery"]["lowestPrice"]["amount"]
            allegro_seller_id = offer["seller"]["id"]
            delivery_cost_currency = offer["delivery"]["lowestPrice"]["currency"]
            price_currency = offer["sellingMode"]["price"]["currency"]
            allegro_category = offer["category"]["id"]

            insert_offer(
                allegro_id, date, name, sold_by_company, available_for_free_delivery,
                price, lowest_delivery_cost, allegro_seller_id, price_currency, delivery_cost_currency,
                allegro_category
            )

        current_offer += OFFER_BATCH
    print("All done")


if __name__ == '__main__':
    main()
