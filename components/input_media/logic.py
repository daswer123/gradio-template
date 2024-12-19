from core.settings_logic import BaseSettingsLogic

# Общие для всех компонентов
class InputMediaLogic(BaseSettingsLogic):
    def get_default_settings(self):
        """Provide specific default settings for this component"""
        return {
            'youtube_quality': '720p',
            'audio_format': 'mp3'
        }
    
    def update_settings(self, youtube_quality, audio_format):
        """Component-specific update method"""
        settings = {
            'youtube_quality': youtube_quality,
            'audio_format': audio_format
        }
        return super().update_settings(**settings)