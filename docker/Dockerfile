FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
        git \
        libgdal-dev \
        postgresql-client-11 \
    && export CPLUS_INCLUDE_PATH=/usr/include/gdal \
    && export C_INCLUDE_PATH=/usr/include/gdal

COPY requirements.txt requirements.txt

RUN echo 'export PATH="${HOME}/.local/bin:$PATH"' >> ~/.bashrc \
    && export PATH="${HOME}/.local/bin:$PATH" \
    && python3.6 -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y ^git \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf \
        node_modules \
        fixtures \
        *.lock \
        *.dist \
        README.md \
        package.json \
        gulpfile.js \
        .gitignore

COPY . /app/

WORKDIR /app/


EXPOSE 8080

CMD ["./manage.py", "runserver", "0.0.0.0:8080"]
