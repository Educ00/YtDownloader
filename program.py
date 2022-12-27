import os
import time
import concurrent.futures
from tqdm import tqdm
from pytube import Playlist
from pytube import YouTube
from pydub import AudioSegment

def download_video(video, destination_folder):
    # Select the highest resolution stream
    highest_resolution_stream = video.streams.filter(progressive=True).order_by('resolution').last()

    # Download the highest resolution stream
    highest_resolution_stream.download(destination_folder)
    
def download_video_as_mp3(video, destination_folder):
    # Get the video's URL using the video_id attribute
    video_id = video.video_id
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    # Create a YouTube object using the video's URL
    yt = YouTube(video_url)

    # Get the first stream and download it to the destination folder
    video = yt.streams.get_highest_resolution()
    video.download(destination_folder)

    # Convert the video to an MP3 file using pydub
    video_path = os.path.join(destination_folder, video.default_filename)
    audio = AudioSegment.from_file(video_path)
    mp3_path = os.path.join(destination_folder, video.default_filename.replace('.mp4', '.mp3'))
    audio.export(mp3_path, format='mp3')

    # Delete the original video file
    os.remove(video_path)

def download_playlist(playlist_url, destination_folder, file_format):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Create a Playlist object using the URL
    playlist = Playlist(playlist_url)

    # Print the number of videos in the playlist
    print('Number Of Videos In Playlist: %s' % len(playlist.video_urls))

    # Use a concurrent.futures.ThreadPoolExecutor to download the videos concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if file_format == 'mp3':
            futures = [executor.submit(download_video_as_mp3, video, destination_folder) for video in playlist.videos]
        elif file_format == 'mp4':
            futures = [executor.submit(download_video, video, destination_folder) for video in playlist.videos]

        # Use tqdm to display a progress bar for the download process
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            # Print any errors that occurred during the download
            if future.exception() is not None:
                print(future.exception())

def run_download_playlist():
    # Prompt the user for the playlist URL
    playlist_url = input('Enter the YouTube playlist URL: ')

    # Prompt the user for the destination folder
    destination_folder = input('Enter the destination folder for the downloaded videos: ')

    # Prompt the user to choose between MP4 or MP3 files
    file_format = input('Enter the desired file format (MP4 or MP3): ')

    download_playlist(playlist_url, destination_folder, file_format)


run_download_playlist()

flag = 0
while flag == 0:
    option = input("Do you want to use the program again?(Y/N): ")
    if option == "Y" or option=="y":
        run_download_playlist()
        flag = 0
    elif option == "N" or option=="n":
        print("Thank you for using this program!")
        flag = 1
        time.sleep(2)
    else:
        flag = 0