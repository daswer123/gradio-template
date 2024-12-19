import gradio as gr
from ..base_layout import BaseLayout
from components.settings import SettingsComponent

class SettingsLayout(BaseLayout):
    """Layout с настройками"""
    
    def setup_components(self):
        """Настройка компонентов"""
        self.components['settings'] = SettingsComponent(
            self.shared_state, 
            "settings"
        )
        self.components['settings1'] = SettingsComponent(
            self.shared_state, 
            "settings1"
        )
    
    def render(self):
        """Рендер layout настроек"""
        with gr.Column():
            self.components['settings'].setup()
            self.components['settings1'].setup()