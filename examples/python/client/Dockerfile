FROM grafana/promtail:latest AS promtail

FROM python:3.10-alpine

RUN apk add build-base

RUN apk add libc6-compat

COPY --from=promtail /usr/bin/promtail /usr/bin/promtail

COPY promtail_config.yml /etc/promtail/config.yml

ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /usr/src/client

RUN apk add build-base

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY init.sh ./

RUN chmod +x init.sh

CMD [ "/usr/src/client/init.sh" ]
