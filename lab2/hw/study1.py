from youtube_dl import YoutubeDL

# Type and run the samples below, one by one
# Result: https://www.dropbox.com/s/cm5m6zitnuwdqbk/Screenshot%202017-12-08%2005.32.02.png?dl=0

# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=9yoXlr8x5xg&frags=pl%2Cwn']) # Remember to put your video in a list, eventhough one video is downloaded
#chess


# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=FxQTY-W6GIo',"https://www.youtube.com/watch?v=Yw5MdbnBQ8s&frags=pl%2Cwn"])
#tientien x eminem


# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=kOCkne-Bku4&frags=pl%2Cwn"])
#lauv


# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Daniel Caesar - Best part (H.E.R.)'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Sam Smith, Leave your lover'])