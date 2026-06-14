from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
def fetch_comments(video_id):

    api_key = os.getenv("API_KEY")
    youtube = build(
        "youtube",
        "v3",
        developerKey=api_key
    )

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    comments = []
    authors = []
    likes = []
    dates = []

    for item in response['items']:

        snippet = item['snippet']['topLevelComment']['snippet']

        comments.append(snippet['textDisplay'])
        authors.append(snippet['authorDisplayName'])
        likes.append(snippet['likeCount'])
        dates.append(snippet['publishedAt'])

    df = pd.DataFrame({
        'author': authors,
        'comment': comments,
        'likes': likes,
        'date': dates
    })

    return df