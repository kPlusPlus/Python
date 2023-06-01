import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

#if os.path.exists('client_secret.json'):
#    print('client_secret. bravo budalama')

# Set up credentials
creds = Credentials.from_authorized_user_file('client_secret.json', SCOPES )

# Build the Gmail API client
service = build('gmail', 'v1', credentials=creds)

try:
    # Fetch the 10 most recent messages in the inbox
    response = service.users().messages().list(userId='me', maxResults=10).execute()

    # Print the subject of each message
    for message in response['messages']:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        print(msg['payload']['headers'][20]['value'])

except HttpError as error:
    print(f"An error occurred: {error}")

