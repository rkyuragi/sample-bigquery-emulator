FROM python:3.11

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install google-cloud-bigquery

COPY app app
WORKDIR /app