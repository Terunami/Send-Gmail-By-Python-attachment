#! /usr/bin/python
#
#   test_gmail.py
#
#                   Jan/03/2019
# ------------------------------------------------------------------
import sys

import argparse
import oauth2client

from gmail_attachment import gmail_attachment_proc 

flags = argparse.ArgumentParser(
    parents=[oauth2client.tools.argparser]
).parse_args()

# ------------------------------------------------------------------
sys.stderr.write("*** 開始 ***\n")
#
mail_from = "example01@gmail.com"
mail_to = "user01@example.or.jp"
#
subject = "Gmail Api Test Jan/03/2019 PM 20:45"
str_message = ""
str_message += "こんにちは。\n"
str_message += "Jan/03/2019 PM 20:45\n"
#
file_attach1 = "text2.txt"
file_attach2 = "text3.csv"
file_attach3 = "text1.txt.zip"
file_attach_list = [file_attach1, file_attach2, file_attach3]
#
for file_attach in file_attach_list:
    sys.stderr.write("file_attach = " + file_attach + "\n")
#
gmail_attachment_proc(mail_from,mail_to,subject,str_message,file_attach_list,flags)
#
sys.stderr.write("*** 終了 ***\n")
# ------------------------------------------------------------------