from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

class VideoService:
    def __init__(self, config):
        self.config = config

    def create_final_video(self, video_path: str, segments: list) -> None:
        """Create final video from selected segments"""
        video = VideoFileClip(video_path)
        clips = []
        
        for seg in segments:
            start = seg["start"]
            end = seg["end"]
            if end - start > 0.1:  # Minimum duration check
                clips.append(video.subclip(start, end))
        
        if clips:
            final_clip = concatenate_videoclips(clips)
            os.makedirs(self.config.EDITED_VIDEO_PATH, exist_ok=True)
            
            output_path = os.path.join(
                self.config.EDITED_VIDEO_PATH,
                os.path.basename(video_path)
            )
            
            final_clip.write_videofile(
                output_path,
                codec="libx264",
                audio_codec="aac"
            )
            final_clip.close()
        
        video.close()