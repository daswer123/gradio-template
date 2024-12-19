import gradio as gr
from .base_shared_state import BaseSharedState

class TestSharedState(BaseSharedState):
    """Основная реализация SharedState для приложения"""
    
    def initialize_elements(self):
        """Инициализация элементов для основного приложения"""
        # Создаем и регистрируем элементы
        test_var = gr.Textbox(
            label="Test Var",
            visible=True
        )
        self.register_element('test_var', test_var)
        
        # Можно добавить другие элементы
        # self.register_element('some_element', gr.some_element(...))
    
    def get_test_var(self):
        """Пример метода для удобного доступа к конкретному элементу"""
        return self.get_element('test_var')