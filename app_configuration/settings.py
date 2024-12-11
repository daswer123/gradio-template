# settings.py
from dataclasses import dataclass
from enum import Enum, auto
from .models import LogLevel

@dataclass
class Settings:
    # Gradio settings
    THEME: str = "default"
    DEBUG: bool = False
    LOG_LEVEL: LogLevel = LogLevel.INFO
    
    SHARE: bool = False
    INBROWSER: bool = True
    
    HOST: str = "localhost"
    PORT: int = 7860
    
    # App settings
    SAVE_PATH: str = "local_data"