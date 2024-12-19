import gradio as gr
from layouts.layout_manager import LayoutManager
from layouts.custom.settings_layout import SettingsLayout
from layouts.custom.settings_layout1 import SettingsLayout1

def create_app():
    # Создаем менеджер layouts
    layout_manager = LayoutManager()
    
    # Регистрируем layouts
    layout_manager.register_layout('settings_layout', SettingsLayout)
    layout_manager.register_layout('settings_layout1', SettingsLayout1)
    
    # Создаем основной интерфейс с табами
    with gr.Blocks() as demo:
        with gr.Tab("Settings"):
            layout_manager.render_layout('settings_layout')
            
        with gr.Tab("Settings1"):
            layout_manager.render_layout('settings_layout1')
            
        with gr.Tab("Audio"):
            # В будущем просто добавим:
            # layout_manager.register_layout('audio', AudioLayout)
            # layout_manager.render_layout('audio')
            gr.Markdown("Audio layout will be here")
            
        with gr.Tab("Video"):
            # И для видео так же:
            # layout_manager.register_layout('video', VideoLayout)
            # layout_manager.render_layout('video')
            gr.Markdown("Video layout will be here")
    
    return demo

if __name__ == "__main__":
    app = create_app()
    app.launch()