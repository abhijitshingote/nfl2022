FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip cron

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

WORKDIR /app

CMD ["/bin/bash","/app/install.sh"]
