import gradio as gr
from typing import Dict, Any
from core.shared_state import SharedState
from ..base_component import BaseComponent
from .logic import InputMediaLogic
from .ui import create_input_media_ui
from .handlers import InputMediaHandlers,SettingsHandlers

class InputMediaComponent(BaseComponent):
    def __init__(self, shared_state: SharedState, component_name: str = "input_media"):
        super().__init__(shared_state, component_name)

        # Используем settings_manager из базового класса
        self.logic = InputMediaLogic(self.component_name, self.settings_manager)
        
    def setup(self):
        # Загружаем текущие настройки
        current_settings = self.logic.load_settings()
        
        # Создаем UI
        ui_elements = create_input_media_ui(current_settings)
        
        # Регистрируем UI элементы в export manager
        self.register_ui_elements(ui_elements)
        
        # Привязываем обработчики
        handlers = InputMediaHandlers(
            self.logic, 
            self.ui_elements, 
            self.shared_state,
            self.state_manager
        )
        handlers.bind_handlers()

        # Создаем обработчик настроек
        settings_handlers = SettingsHandlers(
            self.logic, 
            self.ui_elements, 
            self.shared_state,
            self.state_manager
        )
        settings_handlers.bind_handlers()
        
        return self