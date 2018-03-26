import youtube_dl
from pandas import DataFrame, read_csv
import pandas as pd 
 
options = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]', 
    'audioformat': "mp4",     
    'noplaylist': True,   
}
 # enter the file name -> csv file
preMatchFile = r'prematch.csv' 
postMatchFile = r'postmatch.csv'

readFile = pd.read_csv(preMatchFile)

# print('Value', readFile['video_url'][0])

length = len(readFile['video_url'])

for i in range(0,length):
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([readFile['video_url'][i]])

