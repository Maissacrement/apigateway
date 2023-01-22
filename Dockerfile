FROM docker:20.10.23-cli

WORKDIR /app
COPY . .

RUN apk update &&\
    apk add python3 py3-pip &&\
    pip3 install -r requirement.txt

ENTRYPOINT [ "python3", "/app/exporter.py" ]