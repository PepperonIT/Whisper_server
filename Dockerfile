# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src src
COPY files files

EXPOSE 5001

ENV FLASK_DEBUG=0

CMD [ "python3", "-m" , "flask", "--app=src/upload.py"," run", "--host=0.0.0.0"]