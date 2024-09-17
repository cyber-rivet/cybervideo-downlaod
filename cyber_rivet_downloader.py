#!/usr/bin/env python3

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

def list_formats(url):
    """List available formats for the given URL."""
    try:
        ydl_opts = {
            'quiet': True,
            'listformats': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url)
    except Exception as e:
        print(f"An error occurred while listing formats: {e}")

def download_video(url):
    """Download the video from the given URL."""
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Title: {info_dict.get('title')}")
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Attempting to list available formats...")
        list_formats(url)

def main():
    # Display banner and message
    banner()

    # Prompt user for YouTube URL
    url = input("Please enter the YouTube video URL: ").strip()

    if not url:
        print("No URL provided. Exiting.")
        sys.exit(1)

    # Download the video
    download_video(url)

if __name__ == "__main__":
    main()
