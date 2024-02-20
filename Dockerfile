FROM python:3.10.12

RUN addgroup --system dater_group && adduser --system --group dater


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /dater
WORKDIR /dater

COPY requirements.txt /dater/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /dater/

USER dater