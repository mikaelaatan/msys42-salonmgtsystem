# syntax=docker/dockerfile:1

# install dependencies
FROM python:3.8.10-alpine3.13 AS build-base
RUN pip install --upgrade pip pipenv
WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --prefix="/install" -r requirements.txt

# install mysqlclient
FROM python:3.8.10-alpine3.13
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev ;\
    pip install mysqlclient;\
    apk del .build-deps 

# set official working directory
WORKDIR /usr/src/app

COPY --from=build-base /install usr/src/app/install/
COPY --from=build-base /tmp/requirements.txt usr/src/app/requirements.txt

COPY . /usr/src/app/

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]