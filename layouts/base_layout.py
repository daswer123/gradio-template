import gradio as gr
from core.shared_state import SharedState

class BaseLayout:
    """Базовый класс для различных layouts приложения"""
    def __init__(self):
        self.shared_state = None
        self.components = {}
        
    def initialize(self):
        """Инициализация shared states"""
        self.shared_state = SharedState()
        
    def setup_components(self):
        """Настройка компонентов - переопределяется в наследниках"""
        pass
        
    def render(self):
        """Рендер layout - переопределяется в наследниках"""
        pass
    
    def launch(self):
        """Запуск приложения как самостоятельного интерфейса"""
        self.initialize()
        self.setup_components()
        with gr.Blocks() as demo:
            self.render()
        demo.launch()