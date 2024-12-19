import gradio as gr
from database.database import init_db
from components.shared_state import SharedState
from components.settings import create_settings_component

from managers.settings_manager import SettingsManager

# Инициализация БД
init_db()

with gr.Blocks() as demo:
    shared_state = SharedState()
    settings_manager = SettingsManager()
    
    with gr.Tab("Settings"):
        create_settings_component(shared_state,settings_manager)
    
    # Можно добавить другие табы и компоненты, которые будут использовать эти настройки
    
demo.launch()