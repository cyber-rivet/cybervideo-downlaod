#!/usr/bin/env python3

import os
import sys
from yt_dlp import YoutubeDL

def banner():
    print("""
    __          __  _                            _   __
    \ \        / / | |                          | |  \ \
     \ \  /\  / /__| | ___ ___  _ __ ___   ___ | |_  \ \
      \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \| __|  \ \
       \  /\  /  __/ | (_| (_) | | | | | |  __/| |_    / /
        \/  \/ \___|_|\___\___/|_| |_| |_|\___| \__|  /_/

    Tool: Cyber Rivet
    Description: A stylish Python tool for downloading YouTube videos.
    Made by: Cyber Rivet
    ================================================================
    """)

def download_video(url):
    try:
        ydl_opts = {
            'format': 'best',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Title: {info_dict.get('title')}")
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: cyber_rivet_downloader.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Display banner and message
    banner()

    # Download the video
    download_video(url)

if __name__ == "__main__":
    main()
