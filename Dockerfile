FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]