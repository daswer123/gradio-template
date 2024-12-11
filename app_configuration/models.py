from dataclasses import dataclass
from enum import Enum, auto

class LogLevel(Enum):
    NONE = auto()
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    DEBUG = auto()
