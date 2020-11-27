import email
import imaplib
import re
import os

f = open("mails.txt","r")

Lines = f.readlines()
for line in Lines:

    #extraer id-------
    i = 0
    x = ""
    while x != '<':
        x = line[i]
        i += 1
    start = i
    i = 0
    while x != '>':
        x = line[i]
        i += 1
    end = i-1
    msg_id = line[start:end]
  
    x = re.findall("[0-9]{13}\.[a-f0-9]{13}@Nodemailer|[0-9]{13}\.[a-f0-9]{12}@Nodemailer",msg_id)
    if not x:
        print(msg_id," <- FALSO")
    else:
        print(msg_id, "<<")
        
f.close()

