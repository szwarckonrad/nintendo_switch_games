FROM python:3.7

WORKDIR /scrap

COPY allegro/ /scrap/allegro
COPY common/ /scrap/common

RUN ls -al /scrap
RUN ls -al /scrap/allegro/script

RUN pip3 install -r allegro/requirements.txt

ENV PYTHONPATH /scrap
ENTRYPOINT ["python", "allegro/script/base.py"]
