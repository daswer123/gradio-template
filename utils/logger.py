# utils/logger.py
from datetime import datetime
from enum import Enum, auto
from typing import Optional

class LogLevel(Enum):
    NONE = auto()
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    DEBUG = auto()

class Logger:
    """Enhanced logger with source context"""
    
    # Default settings
    DEFAULT_LEVEL = LogLevel.INFO
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """Singleton pattern implementation"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, source: str = None):
        """Initialize logger with source context"""
        if not self._initialized:
            self._initialized = True
            self._log_level = self.DEFAULT_LEVEL
            self._debug_enabled = False
        
        self.source = source or "Main"

    def _format_message(self, level: LogLevel, message: str) -> str:
        """Format log message with timestamp and source"""
        return f"[{datetime.now()}] [{level.name}] [{self.source}] {message}"

    def set_level(self, level: LogLevel):
        """Set logging level"""
        self._log_level = level

    def set_debug(self, enabled: bool):
        """Enable or disable debug mode"""
        self._debug_enabled = enabled
        if enabled and self._log_level.value < LogLevel.DEBUG.value:
            self._log_level = LogLevel.DEBUG

    def _should_log(self, level: LogLevel) -> bool:
        """Check if message should be logged based on current settings"""
        if self._log_level == LogLevel.NONE:
            return False
        if level == LogLevel.DEBUG and not self._debug_enabled:
            return False
        return level.value <= self._log_level.value

    def log(self, message: str, level: LogLevel = LogLevel.INFO):
        """Generic logging method"""
        if self._should_log(level):
            print(self._format_message(level, message))

    def debug(self, message: str):
        """Log debug message"""
        self.log(message, LogLevel.DEBUG)

    def info(self, message: str):
        """Log info message"""
        self.log(message, LogLevel.INFO)

    def warning(self, message: str):
        """Log warning message"""
        self.log(message, LogLevel.WARNING)

    def error(self, message: str):
        """Log error message"""
        self.log(message, LogLevel.ERROR)

# Пример использования:
if __name__ == "__main__":
    # Создаем логгер для модуля
    logger = Logger("TestModule")
    
    # Установка уровня логирования
    logger.set_level(LogLevel.DEBUG)
    logger.set_debug(True)
    
    # Примеры логирования
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    # Создание логгера для другого модуля
    another_logger = Logger("AnotherModule")
    another_logger.info("This message is from another module")