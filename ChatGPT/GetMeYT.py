import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

def get_youtube_videos(channel_id, api_key):
    """
    This function retrieves a list of videos from a YouTube channel using the YouTube Data API.
    """
    try:
        # authorize the API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        credentials = flow.run_local_server(port=0)

        # build the API client
        youtube = googleapiclient.discovery.build(
            'youtube', 'v3', credentials=credentials, developerKey=api_key)

        # retrieve the list of videos from the channel
        request = youtube.search().list(
            part="id,snippet",
            channelId=channel_id,
            order="date",
            type="video",
            maxResults=50
        )
        response = request.execute()

        # extract the video information from the response
        videos = []
        for item in response['items']:
            video = {
                'id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'thumbnail': item['snippet']['thumbnails']['default']['url']
            }
            videos.append(video)

        return videos

    except googleapiclient.errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None

# Example usage
#channel_id = 'YOUR_CHANNEL_ID'
channel_id = 'PL4efVE8mfQDjQDlBLqaZ9hIhr3_bxZypc'
#api_key = 'YOUR_API_KEY'
api_key = 'AIzaSyATcr89swNwj2IXD8n7PpedPzWqKgGT6_8'
videos = get_youtube_videos(channel_id, api_key)
print(videos)
