from googleapiclient.discovery import build

from utils import get_duration

class YouTube:
    """ fetch and print the video ID of every single video uploaded to a
    particular YouTube channel """
    def __init__(self, api_service_name, api_version, api_key):
        self.api_service_name = api_service_name
        self.api_version = api_version
        self.api_key = api_key
        self.youtube = build(self.api_service_name, self.api_version,
                             developerKey=self.api_key)

    def get_video_ids(self, channel_id):
        """ Get all the video IDs for the given channel """
        channel_details = self.youtube.channels().list(part="contentDetails", id=channel_id).execute()
        playlist_id = channel_details['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        video_ids = []
        next_page = None

        while True:
            response = self.youtube.playlistItems().list(
                playlistId=playlist_id,
                part="snippet",
                maxResults=50,
                pageToken=next_page). \
                execute()
            items_list = response.get('items', None)

            if items_list is None:
                break

            for item in items_list:
                video_id = item['snippet']['resourceId']['videoId']
                video_ids.append(video_id)

            next_page = response.get('nextPageToken')

            if next_page is None:
                break

        return video_ids

    def get_video_stats(self, video_id):
        """ Get all the video IDs for the given channel """
        video_details = self.youtube.videos().list(part="snippet,contentDetails,statistics", id=video_id).execute()
        item = video_details["items"][0]
        return {
            "title": item["snippet"]["title"],
            "publishedAt": item["snippet"]["publishedAt"],
            "duration": get_duration(item["contentDetails"]["duration"]),
            "views": item["statistics"]["viewCount"],
            "likes": item["statistics"]["likeCount"],
            "comments": item["statistics"]["commentCount"]
        }