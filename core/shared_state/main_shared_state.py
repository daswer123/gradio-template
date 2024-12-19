import gradio as gr
from .base_shared_state import BaseSharedState

class SharedState(BaseSharedState):
    """Основная реализация SharedState для приложения"""
    
    def initialize_elements(self):
        """Инициализация элементов для основного приложения"""
        # Создаем и регистрируем элементы
        some_var = gr.Textbox(
            label="Some Var",
            visible=True
        )
        self.register_element('some_var', some_var)
        
        # Можно добавить другие элементы
        # self.register_element('some_element', gr.some_element(...))
    
    def get_some_var(self):
        """Пример метода для удобного доступа к конкретному элементу"""
        return self.get_element('some_var')