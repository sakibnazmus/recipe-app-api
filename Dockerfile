FROM python:3
MAINTAINER Nazmus Sakib

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN addgroup developer
RUN adduser user --disabled-password
RUN usermod -a -G developer user
USER user