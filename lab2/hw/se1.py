from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
connection = urlopen(url)

raw_data = connection.read()
page_content = raw_data.decode()

# Find ROI
soup = BeautifulSoup(page_content, "html.parser")
sec = soup.find("section","section chart-grid")
ul = sec.div.ul

# Extract data
li_list = ul.find_all("li")
# print(li_list)
songs_list = []
for li in li_list:
    b = li.h3.a
    song_title = b.string
    c = li.h4.a
    artist = c.string
    songs = OrderedDict({
        "title":song_title,
        "artist":artist,
    })
    songs_list.append(songs)
# print(songs_list)

# pyexcel.save_as(records=songs_list,dest_file_name="itunesongs.xlsx")

from youtube_dl import YoutubeDL

options = {
    "default_search":"ytsearch",
    "max_downloads": 1,
}
dl = YoutubeDL(options)
for i in songs_list:
    dl.download(i["title"]+i["artist"])