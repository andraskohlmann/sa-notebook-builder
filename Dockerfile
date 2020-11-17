FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python3-ipykernel

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT python -m pytest tests