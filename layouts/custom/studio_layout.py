import gradio as gr

# Base
from ..base_layout import BaseLayout
from core.shared_state import SharedState

# Components
from components.input_media import InputMediaComponent
from components.output_media import OutputMediaComponent

class StudioLayout(BaseLayout):
    """Layout студии с поддержкой инъекции shared state"""
    
    def __init__(self, shared_state: SharedState = None):
        """
        Args:
            shared_state (SharedState, optional): Инстанс shared state для инъекции.
                Если не предоставлен, будет создан стандартный SharedState.
        """
        super().__init__(shared_state)
    
    def setup_components(self):
        """Настройка компонентов"""
        # Создаем компоненты с инъектированным shared state
        self.components['input_media_studio'] = InputMediaComponent(
            self.shared_state, 
            "input_media_studio"
        )
        self.components['output_media_studio'] = OutputMediaComponent(
            self.shared_state, 
            "output_media_studio"
        )
        


    def render(self):
        # Рендерим шейред стейт
        self.shared_state.initialize_elements()

        """Рендер layout студии"""
        with gr.Column():
            # Рендер компонентов
            with gr.Row():
                self.components['input_media_studio'].setup() 
                self.components['output_media_studio'].setup() 
                    