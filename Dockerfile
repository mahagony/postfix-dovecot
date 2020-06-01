FROM alpine:latest

EXPOSE 25/tcp
EXPOSE 143/tcp

RUN apk add --no-cache postfix dovecot

RUN mkdir /var/vmail
RUN chown dovecot:dovecot /var/vmail

COPY etc /etc
COPY start.sh /

RUN chmod 755 /etc/postfix
RUN chmod 600 /etc/postfix/master.cf /etc/postfix/main.cf
RUN chmod 755 /start.sh

RUN newaliases

CMD /start.sh
