import gradio as gr
from ..base_layout import BaseLayout
from components.settings import SettingsComponent
from components.visual import VisualComponent

class SettingsLayout(BaseLayout):
    """Layout с настройками"""
    
    def setup_components(self):
        """Настройка компонентов"""
        self.components['settings'] = SettingsComponent(
            self.shared_state, 
            "settings"
        )
        self.components['visual'] = VisualComponent(
            self.shared_state, 
            "visual"
        )
    
    def render(self):
        """Рендер layout настроек"""
        self.shared_state.initialize_elements()
        with gr.Column():
            self.components['settings'].setup()
            self.components['visual'].setup()