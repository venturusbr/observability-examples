#!/bin/sh
/usr/bin/promtail -config.file /etc/promtail/config.yml &
python main.py