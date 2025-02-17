import os
from dotenv import load_dotenv
from typing import Optional, Literal

load_dotenv()

class Config:
    # API Configuration
    AI_PROVIDER: Literal["openai", "deepseek", "gemini"] = "openai"
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    DEEPSEEK_API_KEY: Optional[str] = os.getenv("DEEPSEEK_API_KEY")
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    
    # Model Configuration
    class Models:
        class OpenAI:
            AUDIO = "whisper-1"
            CHAT = "gpt-4"
            
        class DeepSeek:
            AUDIO = "deepseek-audio-1"
            CHAT = "deepseek-chat"
            
        class Gemini:
            AUDIO = "gemini-pro-vision"
            CHAT = "gemini-pro"
    
    @property
    def ACTIVE_AUDIO_MODEL(self) -> str:
        return {
            "openai": self.Models.OpenAI.AUDIO,
            "deepseek": self.Models.DeepSeek.AUDIO,
            "gemini": self.Models.Gemini.AUDIO
        }[self.AI_PROVIDER]
    
    @property
    def ACTIVE_CHAT_MODEL(self) -> str:
        return {
            "openai": self.Models.OpenAI.CHAT,
            "deepseek": self.Models.DeepSeek.CHAT,
            "gemini": self.Models.Gemini.CHAT
        }[self.AI_PROVIDER]
    
    @property
    def ACTIVE_API_KEY(self) -> str:
        keys = {
            "openai": self.OPENAI_API_KEY,
            "deepseek": self.DEEPSEEK_API_KEY,
            "gemini": self.GEMINI_API_KEY
        }
        if not keys[self.AI_PROVIDER]:
            raise ValueError(f"{self.AI_PROVIDER.title()} API key not found in environment variables")
        return keys[self.AI_PROVIDER]

    SUPPORTED_VIDEO_FORMATS = (".mp4", ".mov", ".avi", ".mkv")
    RAW_VIDEO_PATH = "raw"
    EDITED_VIDEO_PATH = "edited"
    
    # Audio processing settings
    FRAME_DURATION_MS = 30
    PADDING_DURATION_MS = 300
    VAD_AGGRESSIVENESS = 3
    POST_SPEECH_PADDING_SEC = 0.2