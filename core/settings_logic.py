class BaseSettingsLogic:
    """Base class for handling settings logic that can be used across components"""
    def __init__(self, component_name, settings_manager):
        self.component_name = component_name
        self.settings_manager = settings_manager
        self.default_settings = self.get_default_settings()
    
    def get_default_settings(self):
        """Override this method to provide component-specific default settings"""
        return {}
    
    def load_settings(self):
        """Load settings with defaults for the component"""
        return self.settings_manager.load_settings(
            self.component_name,
            self.default_settings
        )
    
    def save_settings(self, settings):
        """Save settings for the component"""
        self.settings_manager.save_settings(
            self.component_name,
            settings
        )
    
    def update_settings(self, **settings):
        """Update settings with provided values"""
        self.save_settings(settings)
        return settings