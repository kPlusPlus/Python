import os
import json
from google.oauth2.credentials import Credentials

def load_user_secrets_from_local(user_secrets_file):
    print("Auth credentials")
    if os.path.exists(user_secrets_file):
        with open(user_secrets_file, 'r') as stream:
            creds_json = json.load(stream)
        creds = Credentials.from_authorized_user_info(creds_json)
        # workaround for
        # https://github.com/googleapis/google-auth-library-python/issues/501
        creds.token = creds_json['token']        
        return creds
    return None


load_user_secrets_from_local('client_secret.json')