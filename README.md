# CONTAINER SMTP+IMAP

Simple container with smtp and imap server.

smtp server = postfix

imap server = dovecot

> podman container run --detach --name=postfix-dovecot --publish=9025:25 --publish=9143:143 postfix-dovecot:latest

Le nom de domaine est 'mahagony4.me'

## imap
le mot de passe pour tous les utilisateurs du domaine est 'test'
