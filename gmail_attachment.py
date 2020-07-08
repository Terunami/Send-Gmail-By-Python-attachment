#
#   gmail_attachement.py
#
#                   Jan/03/2019
# ------------------------------------------------------------------
import httplib2
import os
import sys

import apiclient
from get_credentials import get_credentials_proc
# ------------------------------------------------------------------
import base64
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.base import MIMEBase
import traceback
from email.message import EmailMessage
import imghdr

# ------------------------------------------------------------------
# [6-8-4]:
def attach_image_proc(message,img_data,filename):
    try:
        message.add_attachment(img_data,maintype='image',
            subtype=imghdr.what(None,img_data),filename=filename)
    except Exception as ee:
        sys.stderr.write("*** error *** in message.add_attachment ***\n")
        sys.stderr.write(str(ee) + "\n")
#
    return message
# ------------------------------------------------------------------
# [6-8-6]:
def attach_application_proc(message,data_attach,filename,subtype):
    try:
        message.add_attachment(data_attach,maintype='application',
            subtype=subtype,filename=filename)
    except Exception as ee:
        sys.stderr.write("*** error *** in message.add_attachment ***\n")
        sys.stderr.write(str(ee) + "\n")
#
    return message
# ------------------------------------------------------------------
# [6-8]:
def create_message(mail_from,mail_to,subject,str_message,file_attach):
    message = EmailMessage()
    message.set_content(str_message)
#
    message["From"] = mail_from
    message["To"] = mail_to
    message["Subject"] = subject
    message["Date"] = formatdate(localtime=True)
#
    fp = open(file_attach,'rb')
    img_data = fp.read()
    fp.close()
#
    for suffix in [".pdf",".csv",".json",".xlsx",".zip"]:
        if (file_attach.endswith(suffix)):
            message = attach_application_proc \
                (message,img_data,file_attach,suffix)
#
    for suffix in [".jpg",".png"]:
        if (file_attach.endswith(suffix)):
            message = attach_image_proc \
                (message,img_data,file_attach)
#
    byte_msg = message.as_string().encode(encoding="UTF-8")
    byte_msg_b64encoded = base64.urlsafe_b64encode(byte_msg)
    str_msg_b64encoded = byte_msg_b64encoded.decode(encoding="UTF-8")

    return {"raw": str_msg_b64encoded}
#
# ------------------------------------------------------------------
# [6]:
def gmail_attachment_proc(mail_from,mail_to,subject,str_message,file_attach,flags):
    credentials = get_credentials_proc(flags)
    http = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build("gmail", "v1", http=http)
#
    try:
        result = service.users().messages().send(
            userId=mail_from,
            body=create_message(mail_from,mail_to,subject,str_message,file_attach)
        ).execute()

        print("Message Id: {}".format(result["id"]))

    except apiclient.errors.HttpError:
        print("------start trace------")
        traceback.print_exc()
        print("------end trace------")
#
# ------------------------------------------------------------------