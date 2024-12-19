import gradio as gr
from typing import Dict, Any
from core.shared_state import SharedState
from ..base_component import BaseComponent
from .logic import OutputMediaLogic
from .ui import create_output_media_ui
from .handlers import OutputMediaHandlers

class OutputMediaComponent(BaseComponent):
    def __init__(self, shared_state: SharedState, component_name: str = "output_media"):
        super().__init__(shared_state, component_name)

        # Используем settings_manager из базового класса
        self.logic = OutputMediaLogic(self.component_name, self.settings_manager)
        
    def setup(self):
        # Загружаем текущие настройки
        current_settings = self.logic.load_settings()
        
        # Создаем UI
        ui_elements = create_output_media_ui(current_settings)
        
        # Регистрируем UI элементы в export manager
        self.register_ui_elements(ui_elements)
        
        # Привязываем обработчики
        handlers = OutputMediaHandlers(
            self.logic, 
            self.ui_elements, 
            self.shared_state,
            self.state_manager
        )
        handlers.bind_handlers()

        
        return self