ARG  JAVA_VERSION=11.0-jdk
FROM openjdk:${JAVA_VERSION}-slim-buster

WORKDIR /app

#debian https://packages.debian.org/bullseye/chromium
RUN apt-get update && apt-get install -y \
    wget \
    git \
    unzip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatomic1 \
    libatspi2.0-0 \
    libbrotli1 \
    libc6 \
    libexpat1 \
    libflac8 \
    libfontconfig1 \
    libfreetype6 \
    libjpeg62-turbo \
    liblcms2-2 \
    libminizip1 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libcairo2 \
    #    libgtk-4-1 \
    libnspr4 \
    libnss3 \
    libopenjp2-7  \
    libopus0  \
    libpng16-16 \
    libpulse0 \
    libsnappy1v5 \
    libstdc++6 \
    libwebp6 \
    libwebpdemux2 \
    libwebpmux3 \
    libwoff1  \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxml2 \
    libxnvctrl0 \
    libxrandr2 \
    libxslt1.1 \
    libxtst6 \
    zlib1g \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libpango-1.0-0 \
    libxshmfence1

ARG  GECKODRIVER_VERSION=v0.32.2

# 安装 Firefox 和驱动
RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl

# 设置无头模式
ENV MOZ_HEADLESS=1

