import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import isodate

# get the text which is in the text file key.txt and save it in the variable api_key
with open('key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

# Set up the API client
api_service_name = "youtube"
api_version = "v3"
# api_key = "YOUR_API_KEY"  # Replace with your own API key

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

# Make a request to the API to get popular gaming videos
request = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    chart="mostPopular",
    maxResults=10,  # You can adjust the number of videos you want to retrieve
    videoCategoryId="20",  # Category ID for Gaming
    regionCode="DE"  # Two character code for the country you want to retrieve videos from
)

# Make a request to the API to get popular music videos
# request = youtube.videos().list(
#     part="snippet",
#     chart="mostPopular",
#     maxResults=50,  # You can adjust the number of videos you want to retrieve
#     videoCategoryId="10"  # Category ID for Music
# )

response = request.execute()

# Print video titles
for item in response["items"]:
    print(item["snippet"]["title"])
    print("Channel name:", item["snippet"]["channelTitle"])
    print("View count:", item["statistics"]["viewCount"])
    
    duration = isodate.parse_duration(item["contentDetails"]["duration"])            
    print("Duration:", duration)

    # Get the channel ID for the video
    # channel_id = item["snippet"]["channelId"]
    
    # # Make a request to the API to get the channel information
    # channel_request = youtube.channels().list(
    #     part="snippet,brandingSettings",
    #     id=channel_id
    # )
    
    # channel_response = channel_request.execute()

    # print(channel_response["items"][0]["snippet"]["description"])

    # Print the linked social media profiles and channel links
    # branding_settings = channel_response["items"][0]["brandingSettings"]
    # if "channel" in branding_settings:
    #     print(branding_settings["channel"])
    #     channel_links = branding_settings["channel"]["featuredChannelsUrls"]
    #     print("Linked channels:")
    #     for link in channel_links:
    #         print("Title:", link["title"])
    #         print("URL:", link["url"])
    # if "twitter" in branding_settings:
    #     twitter_handle = branding_settings["twitter"]["twitterHandle"]
    #     print("Twitter handle:", twitter_handle)
    # if "instagram" in branding_settings:
    #     instagram_handle = branding_settings["instagram"]["handle"]
    #     print("Instagram handle:", instagram_handle)

    print("-----------------------")

