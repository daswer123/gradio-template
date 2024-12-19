import gradio as gr
from ..base_layout import BaseLayout
from components.settings import SettingsComponent

class SettingsLayout1(BaseLayout):
    """Layout с настройками"""
    
    def setup_components(self):
        """Настройка компонентов"""
        self.components['settings2'] = SettingsComponent(
            self.shared_state, 
            "settings2"
        )
        self.components['settings3'] = SettingsComponent(
            self.shared_state, 
            "settings3"
        )
    
    def render(self):
        """Рендер layout настроек"""
        with gr.Column():
            self.components['settings2'].setup()
            self.components['settings3'].setup()