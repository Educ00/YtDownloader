import pytube
import re
import time

def download_video():
    url = input("Enter the video link: ")
    yt = pytube.YouTube(url)
    title = yt.title
    title = re.sub(r'[^\w\s-]', '', title)
    title = title.strip().replace(' ', '_')
    name_of_video = f'{title}.mp4'
    
    # Select the highest quality video
    video = yt.streams.get_highest_resolution()
    
    # Prompt the user to enter the output folder
    output_folder = input("Enter the output folder: ")
    
    # Set the output directory and file name
    try:
        video.download(output_path=output_folder, filename=name_of_video)
        print(f'Video downloaded to {output_folder}')
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