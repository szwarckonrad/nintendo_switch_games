import sys
from urllib.parse import urlencode

import requests
from requests import HTTPError

from allegro.script.constants import ALLEGRO_AUTH_URL, COMMON_PARAMS, OFFER_BATCH


def fetch_allegro_token(allegro_auth_string):
    try:
        r = requests.get(
            ALLEGRO_AUTH_URL,
            params={"grant_type": "client_credentials"},
            headers={
                "Authorization": f"Basic {allegro_auth_string}"
            }
        )
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'Http error: {http_err}')
        sys.exit()
    return r.json()["access_token"]


def fetch_offer_count(allegro_token):
    params = {
        "limit": "1",
        "include": ["-items", "searchMeta", "-categories", "-filters", "-sort"],
    }
    params.update(COMMON_PARAMS)
    query = urlencode(params, doseq=True)
    try:
        r = requests.get(
            f"https://api.allegro.pl/offers/listing?{query}",
            headers={
                "Accept": "application/vnd.allegro.public.v1+json",
                "Authorization": f"Bearer {allegro_token}"
            }
        )
    except HTTPError as http_err:
        print(f'Http error: {http_err}')
        sys.exit()

    return r.json()["searchMeta"]["availableCount"]


def fetch_offer_list(allegro_token, offset):
    params = {
        "limit": OFFER_BATCH,
        "include": ["items", "-searchMeta", "-categories", "-filters", "-sort"],
        "offset": offset
    }
    params.update(COMMON_PARAMS)
    query = urlencode(params, doseq=True)
    try:
        r = requests.get(
            f"https://api.allegro.pl/offers/listing?{query}",
            headers={
                "Accept": "application/vnd.allegro.public.v1+json",
                "Authorization": f"Bearer {allegro_token}"
            }
        )
    except HTTPError as http_err:
        print(f'Http error: {http_err}')
        sys.exit()

    return r.json()
