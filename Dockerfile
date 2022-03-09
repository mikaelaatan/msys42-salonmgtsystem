# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster AS build-base

RUN pip install --upgrade pip pipenv

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --prefix="/install" -r requirements.txt


FROM python:3.8-slim-buster AS builder
RUN apt-get update \
 && apt-get install -y --no-install-recommends default-libmysqlclient-dev gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip download mysqlclient==2.0.1 \
 && tar xzf mysqlclient-2.0.1.tar.gz
WORKDIR /mysqlclient-2.0.1
RUN python setup.py bdist_wheel

FROM python:3.8-slim-buster
RUN apt-get update \
 && apt-get install -y --no-install-recommends libmariadb3 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
COPY --from=builder /mysqlclient-2.0.1/dist/mysqlclient-2.0.1-cp38-cp38-linux_x86_64.whl /
RUN pip install /mysqlclient-2.0.1-cp38-cp38-linux_x86_64.whl

WORKDIR /app

COPY --from=build-base /install /usr/local
COPY --from=build-base /tmp/requirements.txt /app/

COPY . /app/
COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["sh","/docker-entrypoint.sh"]
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]