ARG  VERSION=3.9.16.latest
FROM includeno/pythonfirefox:${VERSION}

WORKDIR /app

ADD . /app

CMD python main.py