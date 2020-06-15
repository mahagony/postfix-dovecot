import imaplib
import email
import pprint

imap_host='localhost'
imap_port=9143
imap_user = 'test1@mahagony4.me'
imap_pass = 'test'

imap = imaplib.IMAP4(host=imap_host, port=imap_port)

imap.login(imap_user, imap_pass)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
    print(f'Message: {num}')
    tmp, data = imap.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    for (k, v) in msg.items():
        print(f'{k}:{v}') 
    imap.store(num, '+FLAGS', '\\Deleted')

imap.expunge()

imap.close()
imap.logout()
