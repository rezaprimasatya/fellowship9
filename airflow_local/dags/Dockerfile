FROM python:3.6.15-buster

RUN apt-get update --fix-missing -y \
    && apt-get install -y python3-dev python3-pip build-essential \
    && apt-get install gcc -y \
    && apt-get install sudo -y \ 
    && apt-get clean

RUN adduser --disabled-password --gecos '' airflow

USER airflow
ARG AIRFLOW_USER_HOME=/usr/local/airflow
COPY camp-dev-377801-1f9093438985.json ${AIRFLOW_USER_HOME}/camp-dev-377801-1f9093438985.json

CMD ["echo", "hello world"]