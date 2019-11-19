"""Pulls useful data using the Youtube API."""

import csv
import json

import requests

with open("api_creds.json", "r") as read_file:
    data = json.load(read_file)

api_url = "https://www.googleapis.com/youtube/v3/search?" \
          "channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&part=snippet" \
          "&key={}".format(data["api"])

api_response = requests.get(api_url)
videos = json.loads(api_response.text)

with open("youtube_videos.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["publishedAt",
                         "title",
                         "description",
                         "thumbnailurl"])
    if videos.get("items") is not None:
        for video in videos.get("items"):
            video_data_row = [
                video["snippet"]["publishedAt"],
                video["snippet"]["title"],
                video["snippet"]["description"],
                video["snippet"]["thumbnails"]["default"]["url"]
                ]
            csv_writer.writerow(video_data_row)