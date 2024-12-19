import gradio as gr
from .base_shared_state import BaseSharedState

class SharedState(BaseSharedState):
    """Основная реализация SharedState для приложения"""
    
    def initialize_elements(self):
        """Инициализация элементов для основного приложения"""
        # Создаем и регистрируем элементы
        silent_audio = gr.File(
            label="Silent Audio",
            type="filepath",
            visible=False
        )
        self.register_element('silent_audio', silent_audio)
        
        # Можно добавить другие элементы
        # self.register_element('some_element', gr.some_element(...))
    
    def get_silent_audio(self):
        """Пример метода для удобного доступа к конкретному элементу"""
        return self.get_element('silent_audio')