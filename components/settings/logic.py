from core.settings_logic import BaseSettingsLogic

# Общие для всех компонентов
class SettingsLogic(BaseSettingsLogic):
    def get_default_settings(self):
        """Provide specific default settings for this component"""
        return {
            'volume': 1.0,
            'sample_rate': 44100,
            'output_format': 'wav'
        }
    
    def update_settings(self, volume, sample_rate, output_format):
        """Component-specific update method"""
        settings = {
            'volume': volume,
            'sample_rate': sample_rate,
            'output_format': output_format
        }
        return super().update_settings(**settings)