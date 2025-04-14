"""
Description: Flask server to display embedded YouTube videos from a list of URLs in a text file.
Parameters: None
Returns: Renders an HTML page with embedded videos
Raises: FileNotFoundError if 'videos.txt' is missing
"""

from flask import Flask, render_template
import re

app = Flask(__name__)

VIDEO_FILE = "videos.txt"

def extract_video_id(url: str) -> str:
    """
    Extracts the YouTube video ID from a standard or short URL.
    """
    match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    return match.group(1) if match else None

def get_videos_from_file(file_path: str) -> list[dict[str, str]]:
    """
    Reads video URLs from a file and returns a list of video IDs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            videos = []
            for url in lines:
                url = url.strip()
                video_id = extract_video_id(url)
                if video_id:
                    videos.append({"video_id": video_id})
            return videos
    except FileNotFoundError:
        raise FileNotFoundError(f"Video file '{file_path}' not found.")

@app.route("/")
def index():
    videos = get_videos_from_file(VIDEO_FILE)
    return render_template("index.html", videos=videos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
