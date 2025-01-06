import os
from fastapi import FastAPI, HTTPException, Query
import subprocess

app = FastAPI()

DOWNLOADS_DIR = "downloads"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

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
