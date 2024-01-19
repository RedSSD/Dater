FROM python:3.10.l2

RUN mkdir -p /home/di

RUN addgroup -S di && adduser -S di -G di

ENV HOME=/home/di
ENV APP_HOME=/home/di/app
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . $APP_HOME

RUN chown -R forum:di $APP_HOME

USER di
