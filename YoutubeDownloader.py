from pytube import YouTube

url = "https://www.youtube.com/watch?v=2Vv-BfVoq4g"

my_video = YouTube(url)

# Title of the video
print(my_video.title)

# Thumbnail image of the video
print(my_video.thumbnail_url)

# Download video
video = my_video.streams.get_highest_resolution()
video.download()

print("Downloaded")

