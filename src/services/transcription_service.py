from openai import OpenAI
import tempfile

class TranscriptionService:
    def __init__(self, config):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.config = config

    def transcribe_audio_segment(self, segment_audio_path: str) -> str:
        """Transcribe an audio segment using Whisper"""
        with open(segment_audio_path, "rb") as f:
            transcript = self.client.audio.transcriptions.create(
                model=self.config.WHISPER_MODEL,
                file=f,
                response_format="json"
            )
        transcript_data = transcript.model_dump()
        return transcript_data.get("text", "")

    def transcribe_segments(self, audio, segments: list) -> list:
        """Transcribe all detected segments"""
        transcriptions = []
        for seg in segments:
            start_ms = int(seg["start"] * 1000)
            end_ms = int(seg["end"] * 1000)
            segment_audio = audio[start_ms:end_ms]
            
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                segment_audio.export(tmp.name, format="wav")
                text = self.transcribe_audio_segment(tmp.name)
                
            transcriptions.append({
                "start": seg["start"],
                "end": seg["end"],
                "text": text.strip()
            })
        
        return transcriptions