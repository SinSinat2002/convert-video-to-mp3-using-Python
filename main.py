
import os
from yt_dlp import YoutubeDL

DOWNLOAD_PATH = f'C:/Users/SinaT/Music'

os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Loop to continuously accept YouTube URLs
while True:
    url = input("Enter the YouTube URL: ")
    if url.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    # Download audio using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_PATH}\\%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"File downloaded successfully to {DOWNLOAD_PATH}")
    except Exception as e:
        print(f"An error occurred: {e}")
