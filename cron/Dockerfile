FROM alpine:latest

LABEL MAINTAINER="Nima Javadi nimajavaadi@gmail.com"

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
COPY ./stats.sh /opt/
RUN chmod +x /opt/stats.sh

CMD ["crond", "-f"]
