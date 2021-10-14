FROM python:3.10.0rc2-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
COPY .env .env
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip3 install -r requirements.txt
