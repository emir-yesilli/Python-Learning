from pytube import YouTube

youtube_link = input("Enter YouTube link: ")
path = ""
YouTube(youtube_link).streams.get_lowest_resolution().download(path)
