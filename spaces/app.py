import os
from fastapi import FastAPI, HTTPException, Query
import subprocess

app = FastAPI()

DOWNLOADS_DIR = "downloads"
CONVERTED_DIR = "converted"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(CONVERTED_DIR, exist_ok=True)

def download_space_with_ytdlp(twitter_url: str) -> str:
    try:
        filename = os.path.join(DOWNLOADS_DIR, f"{twitter_url.split('/')[-1]}.mp4")
        
        # Run yt-dlp command
        subprocess.run(
            ["yt-dlp", "-o", filename, "--hls-prefer-native", "--concurrent-fragments", "16", twitter_url],
            check=True
        )
        return filename
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Failed to download: {str(e)}")

def convert_to_mp3(mp4_file_path: str) -> str:

    if not os.path.exists(mp4_file_path):
        raise HTTPException(status_code=404, detail="MP4 file not found")

    base_name = os.path.splitext(os.path.basename(mp4_file_path))[0]
    mp3_file_path = os.path.join(CONVERTED_DIR, f"{base_name}.mp3")

    # Use FFmpeg to convert
    try:
        subprocess.run(
            ["ffmpeg", "-i", mp4_file_path, "-q:a", "0", "-map", "a", "-threads", "4", mp3_file_path],
            check=True
        )

        return mp3_file_path
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"FFmpeg conversion failed: {str(e)}")

@app.post("/download-space")
async def post_download(twitter_url: str):
    
    # Use yt-dlp to download the space
    try:
        file_path = download_space_with_ytdlp(twitter_url)
        return {
            "message": "Download successful",
            "file_path": file_path
        }
    except HTTPException as e:
        return {"error": str(e.detail)}

@app.post("/convert-to-mp3")
def post_convert_to_mp3(mp4_filename: str):

    mp4_file_path = os.path.join(DOWNLOADS_DIR, mp4_filename)

    # Convert to MP3
    mp3_file_path = convert_to_mp3(mp4_file_path)

    return {
        "message": "Conversion successful",
        "mp3_file_path": mp3_file_path,
    }