import csv
import os

import requests

from game_list.script.constants import GAME_LIST_SPREADSHEET_ADDRESS
from game_list.script.insert import insert_game

querystring = {"key": os.environ["GOOGLE_DRIVE_API_KEY"], "mimeType": "text/csv"}

payload = ""
headers = {
    'cache-control': "no-cache",
}

response = requests.request("GET", GAME_LIST_SPREADSHEET_ADDRESS, data=payload, headers=headers, params=querystring)

with open("games_dump.csv", "wb") as f:
    f.write(response.text.encode("utf-8"))

dict_list = []
with open("games_dump.csv", "rt") as f:
    reader = csv.DictReader(f)
    for line in reader:
        dict_list.append(line)


clean_list = []
for release in dict_list:
    try:
        int(release["release"])
        clean_list.append(release)
    except ValueError:
        pass

for game in clean_list:
    gametitle = game["gametitle"]
    release = int(game["release"])
    usadate = game["usadate"]
    jpndate = game["jpndate"]
    eurdate = game["eurdate"]
    ausdate = game["ausdate"]
    usacart = game["usacart"]
    jpncart = game["jpncart"]
    eurcart = game["eurcart"]
    auscart = game["auscart"]
    english = True if game["english"] == "Yes" else False
    notes = game["notes"]

    insert_game(gametitle, release, usadate, jpndate, eurdate, ausdate, usacart, jpncart, eurcart, auscart, english, notes)
