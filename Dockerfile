FROM python:3.7.5-alpine3.10

RUN apk add --update --no-cache libreoffice \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    libreoffice-lang-ja \
    fontconfig \
    msttcorefonts-installer \
    && update-ms-fonts \
    && fc-cache -fv

WORKDIR /workspace

RUN mkdir /usr/share/fonts/ipa-ex-mincho

COPY ./fonts/ipaexm.ttf /usr/share/fonts/ipa-ex-mincho/

RUN chmod 0644 /usr/share/fonts/ipa-ex-mincho/ipaexm.ttf \
    && fc-cache -fv

WORKDIR /api

COPY ./api /api

RUN pip install -r requirements.txt