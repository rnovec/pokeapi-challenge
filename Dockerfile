# pull official base image
FROM python:3.8.0

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#    && apk add jpeg-dev zlib-dev postgresql-dev gcc python3-dev musl-dev gettext
RUN  apt-get update && apt-get install -y gettext libgettextpo-dev

# copy project
COPY ./src/ /usr/src/app/
COPY ./etc/pip/ /usr/src/app/requirements

# lint
RUN pip install --upgrade pip
# RUN pip install flake8
# COPY . /usr/src/app/
# RUN flake8 --ignore=E501,F401 .

# install dependencies
RUN pip install -r requirements/dev_requirements.txt
