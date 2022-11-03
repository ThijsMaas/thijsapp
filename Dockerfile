FROM debian:bullseye-slim

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    python3.9 \
    python3-pip && \
    pip install Flask

COPY flaskapp /opt/app/flaskapp
COPY run.sh /opt/app/

WORKDIR /opt/app

ENTRYPOINT ["bash", "run.sh"]