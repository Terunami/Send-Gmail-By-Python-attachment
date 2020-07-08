#! /usr/bin/python
#
#   test_gmail.py
#
#                   Jan/03/2019
# ------------------------------------------------------------------
import sys

import argparse
import oauth2client

from gmail_attachement import gmail_attachement_proc 

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
file_attach = "federer.png"
file_attach = "in01.csv"
file_attach = "example01.pdf"
file_attach = "federer.jpg"
#
sys.stderr.write("file_attach = " + file_attach + "\n")
#
gmail_attachement_proc(mail_from,mail_to,subject,str_message,file_attach,flags)
#
sys.stderr.write("*** 終了 ***\n")
# ------------------------------------------------------------------