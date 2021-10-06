FROM python:3.9.7-slim-buster AS build-env

ENV APPDIR /srv

WORKDIR ${APPDIR}

RUN apt update
RUN apt install -y curl
RUN pip3 install -U pip poetry

ENV TINI_VERSION v0.19.0
ENV TINI_PATH /usr/bin/tini
RUN curl -sL https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini > $TINI_PATH && \
    chmod +x $TINI_PATH

ENV DOCKERIZE_VERSION v0.6.1
RUN curl -sL https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz  | tar -C /usr/local/bin -xz

COPY pyproject.toml poetry.lock ${APPDIR}/
RUN poetry export -o ${APPDIR}/requirements.txt


FROM python:3.9.7-slim-buster

ENV APPDIR /srv
ENV STORE_DIR /storage

WORKDIR ${APPDIR}

COPY --from=build-env /usr/local/bin /usr/local/bin
COPY --from=build-env /usr/bin/tini /usr/bin/tini
COPY --from=build-env /srv/requirements.txt ${APPDIR}/requirements.txt

COPY ./app ${APPDIR}/app
COPY ./run.sh ${APPDIR}/run.sh

RUN pip3 install -r requirements.txt

ENTRYPOINT ["tini", "--"]
CMD ["dockerize", "./run.sh"]
