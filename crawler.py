import re
import requests
from bs4 import BeautifulSoup

PLAYLIST_URL = 'https://www.youtube.com/watch?v=0yeL0yWMKcg&list=PLjENrTENSbOT_uZ6JF530OvK4z4tQUOAr&index=1'
PLAYLIST_URL1 = 'https://www.youtube.com/watch?v=M9OdStdplBY&list=PLjENrTENSbOT_uZ6JF530OvK4z4tQUOAr&index=301'
PLAYLIST_URL2 = 'https://www.youtube.com/watch?v=QgfPsmTgqJE&list=PLjENrTENSbOT_uZ6JF530OvK4z4tQUOAr&index=501'
PLAYLIST_URL3 = 'https://www.youtube.com/watch?v=DYxLaRPAE2k&list=PLjENrTENSbOT_uZ6JF530OvK4z4tQUOAr&index=701'
PLAYLIST_URL4 = 'https://www.youtube.com/watch?v=bL_SBQ-CM5M&list=PLjENrTENSbOT_uZ6JF530OvK4z4tQUOAr&index=843'



TITLE_START = 0
video_codes = []
video_titles = []
home_score = []
def crawl(url):
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, "html.parser")
    # print(soup)
    for playlist in soup.findAll('div', {'class': 'playlist-videos-container'}):
        # print(playlist)
        for link in playlist.findAll('a'):
            results = link.get('href')
            # print(results)
            a = 'https://www.youtube.com/watch?v=' + results[9:20]
            video_codes.append(a)
            # i += 1
        for title in playlist.findAll('h4'):
            title = title.string.strip()
            title = title.replace("'", "")
            a = title.encode('utf-8')
            # print(a)
            x = a.split(" ")
            # x = x.encode('utf-8')
            j = title.find("-")
            string = x[0] + " " + x[1]
            arr = title[j-1]
            home_score.append(arr)
            # print(j)
            # j = title.find(" ")
            # print(j)
            title = title[TITLE_START:].strip()
            video_titles.append(string)

    # print(i)

def output():
    arr = " "
    for x, y in enumerate(video_codes):
        arr += "\n" + video_titles[x]
    arr = arr[:-1]
    # query = query.encode('utf-8')
    print(arr)

# globali()
crawl(PLAYLIST_URL)
crawl(PLAYLIST_URL1)
crawl(PLAYLIST_URL2)
crawl(PLAYLIST_URL3)
crawl(PLAYLIST_URL4)



output()
