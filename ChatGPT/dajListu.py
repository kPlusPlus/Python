import os
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

# Set the path to your credentials JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'eastern-seeker-301614-9ba1b401ad07.json'

# Authenticate and create a YouTube Data API client
creds = Credentials.from_authorized_user_file(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=creds)

# Retrieve playlists for the authenticated user
playlists = youtube.playlists().list(
    part='snippet',
    mine=True
).execute()

# Print the title and ID of each playlist
for playlist in playlists['items']:
    print(f"Playlist Title: {playlist['snippet']['title']}")
    print(f"Playlist ID: {playlist['id']}")
    print()
