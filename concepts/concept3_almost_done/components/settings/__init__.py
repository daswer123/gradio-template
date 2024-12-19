import gradio as gr
from typing import Dict, Any
from core.shared_state import SharedState
from ..base_component import BaseComponent
from .logic import SettingsLogic
from .ui import create_settings_ui
from .handlers import SettingsHandlers

class SettingsComponent(BaseComponent):
    def __init__(self, shared_state: SharedState, component_name: str = "settings"):
        super().__init__(shared_state, component_name)

        # Теперь используем settings_manager из базового класса
        # и state_manager из базового класса
        
        # Используем settings_manager из базового класса
        self.logic = SettingsLogic(self.component_name, self.settings_manager)
        
    def setup(self):
        # Загружаем текущие настройки
        current_settings = self.logic.load_settings()
        
        # Создаем UI
        self.ui_elements = create_settings_ui(current_settings)
        
        # Привязываем обработчики
        handlers = SettingsHandlers(
            self.logic, 
            self.ui_elements, 
            self.shared_state,
            self.state_manager
        )
        handlers.bind_handlers()
        
        return self