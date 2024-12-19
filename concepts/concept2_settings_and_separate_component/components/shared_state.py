import gradio as gr
from managers.settings_manager import SettingsManager

class SharedState:
    def __init__(self):
        self.settings_manager = SettingsManager()
        self.settings_state = gr.State(self.settings_manager.load_settings())
        
    def get_settings_state(self):
        return self.settings_state

    def get_settings_manager(self):
        return self.settings_manager