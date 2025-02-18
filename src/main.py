from pydub import AudioSegment
import os

from config import Config
from services.audio_service import AudioService
from services.transcription_service import TranscriptionService
from services.llm_service import LLMService
from services.video_service import VideoService
from utils.file_utils import save_json, get_video_files

class VideoProcessor:
    def __init__(self):
        self.config = Config()
        self.audio_service = AudioService()
        self.transcription_service = TranscriptionService(self.config)
        self.llm_service = LLMService(self.config)
        self.video_service = VideoService(self.config)

    def process_video(self, video_path: str) -> None:
        """Process a single video file"""
        print(f"Processing {video_path}")
        base_name = os.path.splitext(os.path.basename(video_path))[0]

        # Extract audio
        temp_audio_file = f"{base_name}_temp_audio.wav"
        self.audio_service.extract_audio(video_path, temp_audio_file)

        # Detect speech segments
        audio = AudioSegment.from_file(temp_audio_file)
        raw_segments = self.audio_service.detect_segments(audio, self.config)
        save_json(raw_segments, f"{base_name}_raw_segments.json")

        # Transcribe segments
        raw_transcription = self.transcription_service.transcribe_segments(
            audio, raw_segments
        )
        save_json(raw_transcription, f"{base_name}_transcription.json")

        # Clean up temporary audio file
        os.remove(temp_audio_file)

        # Get LLM suggestions
        suggestion = self.llm_service.get_suggestion(raw_transcription)
        save_json(suggestion, f"{base_name}_suggestion.json")

        # Create final video
        self.video_service.create_final_video(video_path, suggestion)

    def process_all_videos(self) -> None:
        """Process all videos in the raw directory"""
        video_files = get_video_files(
            self.config.RAW_VIDEO_PATH,
            self.config.SUPPORTED_VIDEO_FORMATS
        )
        
        for video_file in video_files:
            self.process_video(video_file)

def main():
    processor = VideoProcessor()
    processor.process_all_videos()

if __name__ == "__main__":
    main()
