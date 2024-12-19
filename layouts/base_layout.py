import gradio as gr
from core.shared_state import SharedState

class BaseLayout:
    """Базовый класс для различных layouts приложения"""
    def __init__(self, shared_state: SharedState = None):
        """
        Args:
            shared_state (SharedState, optional): Инстанс shared state для инъекции.
                Если не предоставлен, будет создан новый.
        """
        self.shared_state = shared_state
        self.components = {}
        
    def initialize(self):
        """Инициализация shared states если не был предоставлен"""
        if self.shared_state is None:
            self.shared_state = SharedState()
        
        # Инициализируем элементы shared state в контексте Gradio
        self.shared_state.initialize_elements()
        
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