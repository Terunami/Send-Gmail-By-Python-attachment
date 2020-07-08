#
#   get_credentials.py
#
# ------------------------------------------------------------------
import httplib2
import os
import sys

import oauth2client
import argparse
from oauth2client import file, client, tools
# ------------------------------------------------------------------
SCOPES = "https://www.googleapis.com/auth/gmail.send"
CLIENT_SECRET_FILE = "credentials.json"
APPLICATION_NAME = "MyGmailSender"

# ------------------------------------------------------------------
# [6-4]:
def get_credentials_proc(flags):
    script_dir =os.path.abspath(os.path.dirname(__file__)) 
    credential_dir = os.path.join(script_dir, ".credentials")

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,"my-gmail-sender.json")

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = oauth2client.tools.run_flow(flow,store,flags)
        print("Storing credentials to " + credential_path)
#
    return credentials
#
# ------------------------------------------------------------------