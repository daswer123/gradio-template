# state.py
import gradio as gr
from typing import Any, Dict
from .settings import Settings
from utils.database import Database
from utils.logger import Logger
from dataclasses import asdict
from .models import LogLevel

class State:
    """Main state management class for the application"""
    
    def __init__(self):
        """Initialize State with database, settings and module data storage"""
        self.logger = Logger("State")
        self.db = Database()
        self._settings = self._load_settings()
        self._init_components()
        
        self.logger.info("State initialization completed")
        self.logger.debug(f"Current settings: {self.get_all_settings()}")

    def _init_components(self):
        """Initialize core state components"""
        try:
            # Module data state storage
            self.data_state = gr.State({})
            # Shared components storage
            self.shared_components = {}
            self.logger.debug("Components initialized")
        except Exception as e:
            self.logger.error(f"Failed to initialize components: {str(e)}")
            raise

    def _load_settings(self) -> Settings:
        """
        Load settings from DB and sync with defaults
        Returns:
            Settings object with current values
        """
        try:
            settings = Settings()
            default_settings = asdict(settings)
            stored_settings = self.db.get_settings()
            
            if not stored_settings:
                self.logger.info("No stored settings found, initializing defaults")
                self._initialize_default_settings(settings)
                return settings
                
            return self._sync_settings(settings, default_settings, stored_settings)
        except Exception as e:
            self.logger.error(f"Failed to load settings: {str(e)}")
            raise

    def _sync_settings(self, settings: Settings, default_settings: Dict, stored_settings: Dict) -> Settings:
        """
        Synchronize stored settings with default values
        """
        updated_settings = {}
        # Update existing settings
        for key, default_value in default_settings.items():
            try:
                if key not in stored_settings:
                    self.logger.debug(f"Adding missing setting '{key}'")
                    self.db.set_setting(key, str(default_value))
                    updated_settings[key] = default_value
                else:
                    updated_settings[key] = self._convert_setting_value(
                        key, stored_settings[key], default_value, settings
                    )
            except Exception as e:
                self.logger.error(f"Error processing setting {key}: {str(e)}")
                updated_settings[key] = default_value

        # Remove obsolete settings
        self._cleanup_obsolete_settings(stored_settings, default_settings)
        
        # Update settings object
        for key, value in updated_settings.items():
            setattr(settings, key, value)
        
        return settings

    # state.py

    def _convert_setting_value(self, key: str, stored_value: str, default_value: Any, settings: Settings) -> Any:
        """Convert stored setting value to correct type"""
        try:
            field_type = settings.__dataclass_fields__[key].type

            # Специальная обработка для Enum (LOG_LEVEL)
            if key == 'LOG_LEVEL':
                return LogLevel[stored_value]  # Конвертируем строку в Enum

            if field_type == bool:
                return stored_value.lower() == 'true'

            return field_type(stored_value)
        except (ValueError, AttributeError, KeyError) as e:
            self.logger.warning(f"Error converting setting '{key}', using default")
            self.db.set_setting(key, str(default_value))
            return default_value

    def _cleanup_obsolete_settings(self, stored_settings: Dict, default_settings: Dict):
        """Remove obsolete settings from database"""
        for key in stored_settings:
            if key not in default_settings:
                self.logger.debug(f"Removing obsolete setting '{key}'")
                self.db.remove_setting(key)

    def _initialize_default_settings(self, settings: Settings):
        """Save initial settings to database"""
        default_settings = asdict(settings)
        for key, value in default_settings.items():
            if key == 'LOG_LEVEL':
                self.db.set_setting(key, value.name) 
            else:
                self.db.set_setting(key, str(value))
        self.logger.info("Default settings initialized in database")

    def update_setting(self, key: str, value: Any) -> bool:
        """Update setting and save to database"""
        if hasattr(self._settings, key):
            try:
                field_type = self._settings.__dataclass_fields__[key].type
                if field_type == bool and isinstance(value, str):
                    value = value.lower() == 'true'
                else:
                    value = field_type(value)
                
                setattr(self._settings, key, value)
                self.db.set_setting(key, str(value))
                self.logger.info(f"Updated setting '{key}' to: {value}")
                return True
            except (ValueError, AttributeError) as e:
                self.logger.error(f"Error updating setting '{key}': {str(e)}")
                return False
                
        self.logger.warning(f"Attempted to update non-existent setting '{key}'")
        return False

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get setting value"""
        value = getattr(self._settings, key, default)
        if value is None and default is not None:
            self.logger.debug(f"Setting '{key}' not found, using default: {default}")
        return value

    def get_all_settings(self) -> Dict:
        """Get all settings"""
        return asdict(self._settings)

    def reset_settings(self):
        """Reset settings to defaults"""
        self.logger.info("Resetting all settings to defaults...")
        self.db.clear_settings()
        self._settings = Settings()
        self._initialize_default_settings(self._settings)
        self.logger.info("Settings reset completed")

    def update(self, module: str, data: Dict[str, Any]):
        """Update module data"""
        current_state = self.data_state.value
        if module not in current_state:
            current_state[module] = {}
        current_state[module].update(data)
        self.data_state.value = current_state
        self.logger.debug(f"Updated state for module '{module}' with data: {data}")

    def get(self, module: str, key: str = None) -> Any:
        """Get module data"""
        state_data = self.data_state.value
        if module not in state_data:
            self.logger.debug(f"No data found for module '{module}'")
            return None
        if key:
            value = state_data[module].get(key)
            if value is None:
                self.logger.debug(f"No data found for key '{key}' in module '{module}'")
            return value
        return state_data[module]

    def register_component(self, name: str, component: Any):
        """Register component for inter-module communication"""
        self.shared_components[name] = component
        self.logger.debug(f"Registered component '{name}'")

    def get_component(self, name: str) -> Any:
        """Get registered component"""
        component = self.shared_components.get(name)
        if component is None:
            self.logger.debug(f"Component '{name}' not found")
        return component

    def clear_module_data(self, module: str):
        """Clear all module data"""
        current_state = self.data_state.value
        if module in current_state:
            del current_state[module]
            self.data_state.value = current_state
            self.logger.debug(f"Cleared all data for module '{module}'")

    def has_module_data(self, module: str) -> bool:
        """Check if module has data"""
        return module in self.data_state.value