# from pytube import YouTube

# link =input("Enter the Link to Downlaod  ")
# # link2 ='https://youtu.be/omaZvc2rEPM?si=NRl78SobvbNLjqVY'
# youtube = YouTube(link)
# # print(youtube.title)
# # print(youtube.thumbnail_url)

# # vidio = youtube.streams.all()   #All fromate 

# vidio = youtube.streams.filter(only_audio=True)   # For audio only 
# vid = list(enumerate(vidio))
# for i, k in vid:
#     print(i+1, k)
# print()
# strm  = int(input("Enter :"))
# vidio[strm].download()
# print("Downloaded...")


# for playlist

from pytube import Playlist
palylst = Playlist(input("Enter the Playlist link :  "))

print(f"Downloading : {palylst.title}")

for i in palylst.videos:
    i.streams.first().downlaod()