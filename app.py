import gradio as gr
from layouts.layout_manager import LayoutManager
from layouts.custom.studio_layout import StudioLayout
from core.shared_state import SharedState, TestSharedState

def create_app():
    # Создаем менеджер layouts
    layout_manager = LayoutManager()
    
    # Вариант 1: Использование стандартного SharedState
    layout_manager.register_layout('studio_layout', StudioLayout, SharedState)
    
    # Вариант 2: Использование кастомного SharedState
    # layout_manager.register_layout('studio_layout_custom', StudioLayout, TestSharedState)
    
    
    # Создаем основной интерфейс с табами
    with gr.Blocks() as demo:
        with gr.Tab("Studio (Standard)"):
            layout_manager.render_layout('studio_layout')
            
    return demo

if __name__ == "__main__":
    app = create_app()
    app.launch()