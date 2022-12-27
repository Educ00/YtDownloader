import pytube
import re
import time

def get_video_title(url):
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Return the video title
    return yt.title

def download_video():
    url=(str)(input('Digite o video a fazer download: '))
    
    outputFolder=(str)(input('Digite a pasta do output: '))
    
    # Clean up the video title to make it a valid file name
    title = get_video_title(url)
    title = re.sub(r'[^\w\s-]', '', title)
    title = title.strip().replace(' ', '_')
    nameOfVideo = f'{title}.mp4'
    
    # Create a YouTube object using the URL
    yt = pytube.YouTube(url)

    # Select the highest quality video
    video = yt.streams.get_highest_resolution()

    # Set the output directory and file name
    try:
        video.download(output_path=outputFolder, filename=nameOfVideo)
    except Exception as e:
        print(f'An error occurred while downloading the video: {e}')

download_video()

flag=0

while(flag==0):
    tempFlag=(str)(input('Deseja fazer download de outro video?(S/N): '))
    
    if(tempFlag=='S'):
        download_video()
        flag=0
    if(tempFlag=='N'):
        flag=1
        print('Obrigado por usar o programa! A encerrar...')
        
time.sleep(3)