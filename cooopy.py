from __future__ import print_function
import httplib2
import os
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
from httplib2 import Http
from email import encoders
from apiclient import errors
from datetime import date
from apiclient.discovery import build
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
credentials = get_credentials()
service = build('gmail', 'v1', http=credentials.authorize(Http()))

def send_message(service, user_id, message):
  try:
    message = service.users().messages().send(userId=user_id, body=message).execute()

    print('Message Id: %s' % message['id'])

    return message
  except Exception as e:
    print('An error occurred: %s' % e)
    return None

def create_message_with_attachment(sender, to, subject, message_text, file):
  message = MIMEMultipart()
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject

  msg = MIMEText(message_text,"html")
  message.attach(msg)

  content_type, encoding = mimetypes.guess_type(file)

  if content_type is None or encoding is not None:
    content_type = 'application/octet-stream'

  main_type, sub_type = content_type.split('/', 1)

  if main_type == 'text':
    fp = open(file, 'rb')
    msg = MIMEText(fp.read().decode("utf-8"), _subtype=sub_type)
    fp.close()
  elif main_type == 'image':
    fp = open(file, 'rb')
    msg = MIMEImage(fp.read(), _subtype=sub_type)
    fp.close()
  elif main_type == 'audio':
    fp = open(file, 'rb')
    msg = MIMEAudio(fp.read(), _subtype=sub_type)
    fp.close()
  else:
    fp = open(file, 'rb')
    msg = MIMEBase(main_type, sub_type)
    msg.set_payload(fp.read())
    encoders.encode_base64(msg)
    fp.close()
  msg.add_header('Content-Disposition', 'attachment', filename="%s_uloha%s" %(sub_a[who].lower(),pripona))
  message.attach(msg)

  return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

real = open("contacts_db.txt","r",encoding="utf-8")
to_transpose = real.read().split("\n")
real.close()
def add_to_db(name,subject,suffix_of_subject,email):
    real = open("contacts_db.txt","a",encoding="utf-8")
    real.write("\n%s:%s:%s:%s" %(name,subject,suffix_of_subject,email))
    real.close()

def index_del():
    real = open("contacts_db.txt","r",encoding="utf-8")
    data = real.read().split("\n")
    real.close()
    for i in range(len(data)):
        print("%i) %s"%(i,data[i]))
    index = int(input("Index na vymazanie? "))
    real = open("contacts_db.txt","w",encoding="utf-8")
    for i in range(len(data)):
        if i != index and i != len(data)-1:
            real.write("%s\n"%(data[i]))
        elif i != index and i == len(data)-1:
            real.write("%s"%(data[i]))
    real.close()

modify_db = str(input("Pre pridanie do databázy stlačte \"1\", pre odobranie \"2\"")) == "1"
if modify_db == "1":
    ask = input("Oddelte znakom \":\"").split(":")
    add_to_db(ask[0],ask[1],ask[2],ask[3])
elif modify_db == "2":
    index_del()

resolved = open("resolved.txt","r",encoding="utf-8")
res = int(resolved.read())
resolved.close()
print("Current value of completed tasks is: %i"%(res),end=". ")
override = str(input("Do you wish to override this number? Yes/No/Correct ")).lower()
if override == "yes":
    res = res+int(input("+Number? "))
elif override == "correct":
    res = res-int(input("-Number? "))
else:
    res = res+1
resolved = open("resolved.txt","w",encoding="utf-8")
resolved.write(str(res))
resolved.close()

today = date.today()
dte = today.strftime("%d.%m.%Y")

teacher, adr, sub_a, sub = [],[],[],[]
for i in range(len(to_transpose)):
    teacher.append(to_transpose[i].split(":")[0])
    sub_a.append(to_transpose[i].split(":")[1])
    sub.append(to_transpose[i].split(":")[2])
    adr.append(to_transpose[i].split(":")[3])

r = 0
for i in teacher:
  r+=1
  print(r,") ",i, sep="")
who = int(input("Číslo vybraného učiteľa: "))-1
pripona = str(input("Prípona súboru?"))
if pripona[0] == ".":
  file_name = "send"+pripona
else:
  file_name = "send."+pripona
a = "Riešenie úlohy z %s" %sub[who]
b = "Dobrý deň,<br>Posielam Vám vypracovanú úlohu z %s.<br><br>%s, %s %s #%i<br> Sent via gmail api, <a href=\"https://github.com/oguh43/bilicka/blob/master/gmail.py\">sauce</a>." %(sub[who],teacher[0],sub_a[0],dte,res)

mine = create_message_with_attachment(adr[0],adr[who],a,b,file_name)
testSend = send_message(service, 'me', mine)

"""
!!! DO NOT NAME THIS FILE email.py , IT MESSES UP THE LIBRARIES USED!!!
File name:
file MUST be named send   <----- will be renamed in the email to (for example): biologia_uloha.docx
the extension does NOT matter, you will be asked about it. (you can enter it with or without the dot at the start)
Example database and counter syntax:
contacts_db.TXT:
your_name:classroom:place_holder:your_email
teacher_name:subject:subject_with_suffix:email
teacher_name:subject:subject_with_suffix:email
teacher_name:subject:subject_with_suffix:email
your_name will be put into the email as signature
classroom is a part of the signature
your_email, from where the email will be sent
placeholder, can NOT be blank. Enter some string like Test
subject, for example: Informatika
subject_with_suffix, for example: Informatiky
!MAKE SURE THERE IS NO NEWLINE UPON CREATION, THE PROGRAM WILL NOT PLACE ONE THERE!
resolved.TXT:
0
the number will be incremented by one each time and saved, can be overwritten if you chose so, or "corrected"(substract from it)
!MAKE SURE THERE IS NO NEWLINE UPON CREATION, THE PROGRAM WILL NOT PLACE ONE THERE!
todo:
    1) Maybe rework the database to use a dictonary instead of lists, with names as keys and the rest as values
    2) Incorporate resolved.TXT into contacts_db.TXT at the place of placeholder
"""
