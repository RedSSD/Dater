FROM python:3.10.12

RUN addgroup -S dater
RUN adduser -S dater -G dater

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /dater
WORKDIR /dater

COPY requirements.txt /dater/

RUN pip install --upgrade
RUN pip install -r requirements.txt

ADD . /dater/

USER dater