import email
import imaplib
import re
import os

user_mail = input("USER MAIL: ")
user_password = input("PASSWORD: ")
server = "imap.gmail.com"
port = 993

cont_mail = 0
cont_mail_limit = 200

cont_obj = 0
cont_obj_limit = 20
objetivo = "no-reply@patreon.com"

f = open("mails.txt","w")

#conectar a servidor y acceder al inbox
mail = imaplib.IMAP4_SSL(server,port)
mail.login(user_mail, user_password)

#sleeccionar inbox------
mail.select("inbox")

status, data = mail.search(None, 'ALL')
mail_ids = []
for block in data:
    mail_ids += block.split()
for i in mail_ids:
    status, data = mail.fetch(i, '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_subject = message['subject']
            mail_id = message['Message-ID']
            mail_reply = message['Reply-To']
            mail_date = message['Date']

            print(f'From: {mail_from}')
            print(f'ID: {mail_id}')

            if mail_reply == objetivo:
                f.write(f'ID: {mail_id} ')          
                f.write(f'From: {mail_from}')
                f.write(f'Fecha: {mail_date}')
                f.write("\n")
                cont_obj += 1

            cont_mail += 1

    if cont_obj == cont_obj_limit or cont_mail == cont_mail_limit:
        break

print("\nRevisados ",cont_mail," mails\n")
print("Se hayaron: ",cont_obj, "mail de ",objetivo)

f.close()