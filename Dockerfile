FROM alpine:3.10

RUN apk add --update --no-cache libreoffice \
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