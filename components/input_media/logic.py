from core.settings_logic import BaseSettingsLogic
# from scripts.media_scripts import MediaManager


# Общие для всех компонентов
class InputMediaLogic(BaseSettingsLogic):
    def __init__(self, component_name, settings_manager):
        super().__init__(component_name, settings_manager)
        # self.media_manager = MediaManager()


    # Media part
    def process_input_media(self, input_media, input_microphone, input_youtube_url):
        return None, None
    
    # Extra
    def clear_input_media(self):
        return None, None, None

    # Settings part
    def get_default_settings(self):
        """Provide specific default settings for this component"""
        return {
            'youtube_quality': 'high',
            'audio_format': 'mp3'
        }
    
    def update_settings(self, youtube_quality, audio_format):
        """Component-specific update method"""
        settings = {
            'youtube_quality': youtube_quality,
            'audio_format': audio_format
        }
        return super().update_settings(**settings)