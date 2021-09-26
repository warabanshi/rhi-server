FROM python:3.9.7

ENV APPDIR /srv
ENV STORE_DIR /storage

WORKDIR ${APPDIR}

RUN apt update
RUN apt install -y curl gcc musl-dev libffi-dev libssl-dev
RUN pip3 install -U pip poetry

ENV TINI_VERSION v0.19.0
ENV TINI_PATH /usr/bin/tini
RUN curl -sL https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini > $TINI_PATH && \
    chmod +x $TINI_PATH

ENV DOCKERIZE_VERSION v0.6.1
RUN curl -sL https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz  | tar -C /usr/local/bin -xz

COPY pyproject.toml poetry.lock ${APPDIR}/
RUN poetry config virtualenvs.create false && \
    poetry install -n

COPY ./ ${APPDIR}/

ENTRYPOINT ["tini", "--"]
CMD ["dockerize", "./run.sh"]
