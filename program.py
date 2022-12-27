import os
import time
from pytube import Playlist

def downloadPlaylist():
    # Prompt the user for the playlist URL
    playlist_url = input('Enter the YouTube playlist URL: ')

    # Prompt the user for the destination folder
    destination_folder = input('Enter the destination folder for the downloaded videos: ')

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Create a Playlist object using the URL
    playlist = Playlist(playlist_url)

    # Print the number of videos in the playlist
    print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

    # Iterate through the videos in the playlist
    for video in playlist.videos:
        # Select the highest resolution stream
        highest_resolution_stream = video.streams.filter(progressive=True).order_by('resolution').last()

        # Download the highest resolution stream
        highest_resolution_stream.download(destination_folder)

downloadPlaylist()

flag = 0
while flag == 0:
    option = input("Do you want to use the program again?(Y/N): ")
    if option == "Y" or option=="y":
        downloadPlaylist()
        flag = 0
    elif option == "N" or option=="n":
        print("Thank you for using this program!")
        flag = 1
        time.sleep(2)
    else:
        flag = 0