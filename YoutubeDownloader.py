from pytube import YouTube
# Enter the url of video you want to download
url = ""

my_video = YouTube(url)

# Title of the video
print(my_video.title)

# Thumbnail image of the video
print(my_video.thumbnail_url)

# Download video
video = my_video.streams.get_highest_resolution()
video.download()

print("Downloaded")

