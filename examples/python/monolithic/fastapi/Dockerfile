FROM grafana/promtail:latest AS promtail

FROM python:3.10-alpine

RUN apk add build-base

# RUN wget -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
#     wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.34-r0/glibc-2.34-r0.apk && \
#     apk add --no-cache --force-non-repo glibc-2.34-r0.apk && \
#     rm glibc-2.34-r0.apk

# COPY --from=promtail /usr/lib/x86_64-linux-gnu/libsystemd.so /usr/local/lib/libsystemd.so
# COPY --from=promtail /lib/x86_64-linux-gnu/liblzma.so.5 /usr/local/lib/liblzma.so.5
# COPY --from=promtail /usr/lib/x86_64-linux-gnu/libzstd.so.1 /usr/local/lib/libzstd.so.1
# COPY --from=promtail /usr/lib/x86_64-linux-gnu/liblz4.so.1 /usr/local/lib/liblz4.so.1
# COPY --from=promtail /usr/lib/x86_64-linux-gnu/libgcrypt.so.20 /usr/local/lib/libgcrypt.so.20
# COPY --from=promtail /lib/x86_64-linux-gnu/libgpg-error.so.0 /usr/local/lib/libgpg-error.so.0

RUN apk add libc6-compat

COPY --from=promtail /usr/bin/promtail /usr/bin/promtail

COPY promtail_config.yml /etc/promtail/config.yml

ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /usr/src/fastapi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY init.sh ./

RUN chmod +x init.sh

CMD [ "/usr/src/fastapi/init.sh" ]
