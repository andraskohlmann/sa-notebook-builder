FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT pytest