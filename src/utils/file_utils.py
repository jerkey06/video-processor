import json
import os

def save_json(data: dict, filename: str) -> None:
    """Save data to JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_video_files(directory: str, supported_formats: tuple) -> list:
    """Get all video files from directory"""
    video_files = []
    for file in os.listdir(directory):
        if file.lower().endswith(supported_formats):
            video_files.append(os.path.join(directory, file))
    return video_files