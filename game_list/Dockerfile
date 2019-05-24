FROM python:3.7

WORKDIR /scrap

COPY game_list/ /scrap/game_list
COPY common/ /scrap/common

RUN pip3 install -r game_list/requirements.txt

ENV PYTHONPATH /scrap
ENTRYPOINT ["python", "game_list/script/base.py"]
