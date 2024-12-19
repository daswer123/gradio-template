import gradio as gr
from typing import Dict, Any
from core.shared_state import SharedState
from ..base_component import BaseComponent
from .logic import VisualLogic
from .ui import create_visual_ui
from .handlers import VisualHandlers

class VisualComponent(BaseComponent):
    def __init__(self, shared_state: SharedState, component_name: str = "visual"):
        super().__init__(shared_state, component_name)
        
        # Инициализируем логику
        self.logic = VisualLogic(self.component_name, self.settings_manager)
        
    def setup(self):
        # Создаем UI элементы
        ui_elements = create_visual_ui()
        
        # Регистрируем UI элементы в export manager
        self.register_ui_elements(ui_elements)
        
        # Привязываем обработчики
        handlers = VisualHandlers(
            self.logic, 
            self.ui_elements, 
            self.shared_state,
            self.state_manager
        )
        handlers.bind_handlers()
        
        return self