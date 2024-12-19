import gradio as gr
from core.shared_state import SharedState
from components.settings import SettingsComponent
from core.state_manager import StateManager

def initialize_app():
    # Теперь нам нужен только shared_state
    shared_state = SharedState()
    state_manager = StateManager()
    return shared_state, state_manager

def create_app(shared_state, state_manager):
    # Инциализируем компоненты только с shared_state и именем
    settings_component = SettingsComponent(shared_state, "settings")
    settings_component1 = SettingsComponent(shared_state, "settings1")

    # Глобальный стейт теперь доступен через компонент
    global_state = state_manager.get_global_state()

    with gr.Blocks() as demo:
        # Глобальный стейт теперь доступен через компонент        
        with gr.Tab("Settings"):
            settings_component.setup()
        with gr.Tab("Settings1"):
            settings_component1.setup()
    
    return demo

if __name__ == "__main__":
    shared_state, state_manager = initialize_app()
    app = create_app(shared_state, state_manager)
    app.launch()