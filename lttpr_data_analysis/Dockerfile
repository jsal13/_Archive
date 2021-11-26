FROM debian:stretch-slim

# THIS REQUIRES A LTTP (J) 1.0 RELEASE SAVED
# IN ROOT AS lttp.sfc
COPY alttp_vt_randomizer /src
COPY lttp.sfc /src
WORKDIR /src

RUN apt-get update \
    && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    gnupg \
    software-properties-common \
    unzip \
    wget \
    zip\
    && curl -fsSL https://packages.sury.org/php/apt.gpg | apt-key add - \
    && add-apt-repository "deb https://packages.sury.org/php/ $(lsb_release -cs) main" \
    && apt update \
    && apt-get install -y \
    php7.2-bcmath \
    php7.2-cli \
    php7.2-common \
    php7.2-curl \
    php7.2-dom \
    php7.2-mbstring \
    php7.2-zip \
    && wget https://raw.githubusercontent.com/composer/getcomposer.org/76a7060ccb93902cd7576b67264ad91c8a2700e2/web/installer -O - -q | php -- \
    && php composer.phar install 