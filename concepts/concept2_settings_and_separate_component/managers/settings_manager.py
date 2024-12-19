from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from database.models import Settings
from database.database import SessionLocal

class SettingsManager:
    def __init__(self):
        self._defaults = {
            'volume': 1.0,
            'sample_rate': 44100,
            'output_format': 'wav'
        }

    def get_defaults(self) -> Dict[str, Any]:
        return self._defaults.copy()

    def load_settings(self) -> Dict[str, Any]:
        with SessionLocal() as db:
            settings = db.query(Settings).first()
            if not settings:
                return self.get_defaults()
            
            return {
                'volume': settings.volume,
                'sample_rate': settings.sample_rate,
                'output_format': settings.output_format
            }

    def save_settings(self, settings_dict: Dict[str, Any]) -> None:
        with SessionLocal() as db:
            settings = db.query(Settings).first()
            if not settings:
                settings = Settings()
                db.add(settings)
            
            for key, value in settings_dict.items():
                setattr(settings, key, value)
            
            db.commit()

    def update_setting(self, key: str, value: Any) -> Dict[str, Any]:
        current_settings = self.load_settings()
        current_settings[key] = value
        self.save_settings(current_settings)
        return current_settings