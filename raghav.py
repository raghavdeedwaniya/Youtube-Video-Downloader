from pytube import YouTube

SAVE_PATH = "D:\yt video"

link = input("input your video link: ")

youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_video=True)
# videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

str = int(input("enter : "))
print(f"Downloading : {youtube_1.title}" )
videos[str].download(SAVE_PATH)

print("successfully")


pass

exit()