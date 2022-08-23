FROM python:3.10-alpine

WORKDIR /usr/src/client

RUN apk add build-base

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

CMD [ "python", "./main.py"]
