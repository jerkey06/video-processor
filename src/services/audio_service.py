from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import webrtcvad
import tempfile
import os

class AudioService:
    @staticmethod
    def extract_audio(video_path: str, audio_path: str) -> None:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, logger=None)
        video.close()

    @staticmethod
    def detect_segments(audio: AudioSegment, config) -> list:
        """Detect speech segments using voice activity detection (VAD)"""
        # Convert audio to proper format
        audio = audio.set_channels(1)
        if audio.frame_rate not in (8000, 16000, 32000, 48000):
            audio = audio.set_frame_rate(16000)
        
        sample_rate = audio.frame_rate
        sample_width = audio.sample_width
        raw_audio = audio.raw_data

        vad = webrtcvad.Vad(config.VAD_AGGRESSIVENESS)
        frame_size = int(sample_rate * config.FRAME_DURATION_MS / 1000)
        frame_bytes = frame_size * sample_width

        # Process frames
        frames = []
        for i in range(0, len(raw_audio) - frame_bytes + 1, frame_bytes):
            frame = raw_audio[i:i + frame_bytes]
            timestamp = i / (sample_rate * sample_width)
            frames.append((timestamp, frame))

        # Detect speech in frames
        speech_flags = []
        for timestamp, frame in frames:
            try:
                is_speech = vad.is_speech(frame, sample_rate)
            except Exception as e:
                print(f"Error processing frame at {timestamp:.2f} sec: {e}")
                is_speech = False
            speech_flags.append((timestamp, is_speech))

        # Aggregate into segments
        segments = []
        segment_start = None
        last_speech_timestamp = None

        for timestamp, is_speech in speech_flags:
            if is_speech:
                if segment_start is None:
                    segment_start = timestamp
                last_speech_timestamp = timestamp
            elif segment_start is not None and last_speech_timestamp is not None:
                segments.append({
                    "start": segment_start,
                    "end": last_speech_timestamp + config.POST_SPEECH_PADDING_SEC
                })
                segment_start = None
                last_speech_timestamp = None

        if segment_start is not None:
            total_duration = len(raw_audio) / (sample_rate * sample_width)
            segments.append({"start": segment_start, "end": total_duration})

        # Merge close segments
        merged_segments = []
        if segments:
            current = segments[0]
            for seg in segments[1:]:
                if seg["start"] - current["end"] < config.PADDING_DURATION_MS / 1000.0:
                    current["end"] = seg["end"]
                else:
                    merged_segments.append(current)
                    current = seg
            merged_segments.append(current)

        return merged_segments