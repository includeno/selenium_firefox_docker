ARG  VERSION=3.9.16.latest
FROM includeno/pythonfirefox:${VERSION}

WORKDIR /app

ADD . /app

# Install pip requirements
RUN /bin/sh -c ' cd /app && python -m pip install -r requirements.txt '

CMD python main.py