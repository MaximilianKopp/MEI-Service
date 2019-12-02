FROM python:3-alpine

MAINTAINER Maximilian Kopp

ENV PYTHONPATH=/app

COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "gateway.py"]








