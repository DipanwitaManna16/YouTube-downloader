# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:51:48 2020

@author: DELL
"""

#import libraries
from pytube import YouTube

#accepting input from user
link = input("Enter the link :")
yt = YouTube(link)

#Revealing various Information about the Video
#Title of video
print("Title:",yt.title)
#Number of views of video
print("Number of views:" ,yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)

#printing all the available streams
print(yt.streams)

#Filtering the audio-stream
#print(yt.streams.filter(only_audio=True))

#Filtering the video-stream
#print(yt.streams.filter(only_video=True))

#filtering out progressive streams first
#print(yt.streams.filter(progressive=True))

#highest resolution progressive stream 
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download('YouTube Downloaded Videos')
print("Download completed!!") 






