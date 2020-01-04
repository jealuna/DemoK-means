FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY VacacionesClustering/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/