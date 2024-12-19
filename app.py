import gradio as gr
from layouts.layout_manager import LayoutManager
from layouts.custom.settings_layout import SettingsLayout

def create_app():
    # Создаем менеджер layouts
    layout_manager = LayoutManager()
    
    # Регистрируем layouts
    layout_manager.register_layout('settings_layout', SettingsLayout)
    
    # Создаем основной интерфейс с табами
    with gr.Blocks() as demo:
        with gr.Tab("Settings"):
            layout_manager.render_layout('settings_layout')

    return demo

if __name__ == "__main__":
    app = create_app()
    app.launch()