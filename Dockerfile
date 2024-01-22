FROM python:3.10.l2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /di
COPY requirements.txt /di/

RUN apt update && apt upgrade
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /di/





