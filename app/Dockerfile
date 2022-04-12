# syntax=docker/dockerfile:1

FROM python:3.9.0-alpine3.12 AS build-base

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip pipenv

# install dependencies
WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --prefix="/install" -r requirements.txt

# install mysqlclient
FROM python:3.9.0-alpine3.12
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev ;\
    pip install mysqlclient;\
    apk del .build-deps 

# set official working directory
WORKDIR /usr/src/app

# copies dependencies to local
COPY --from=build-base /install /usr/local
COPY --from=build-base /tmp/requirements.txt usr/src/app/requirements.txt


COPY . /usr/src/app/

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]