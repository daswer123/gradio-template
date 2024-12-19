import gradio as gr
from components.shared_state import SharedState
from components.input_audio import create_input_audio_component
from components.output_files import create_output_files_component

with gr.Blocks() as demo:
    shared_state = SharedState()
    
    with gr.Tab("Audio"):
        gr.Markdown("Мы что-то делаем с аудио.")
        create_input_audio_component(shared_state)
        create_output_files_component(shared_state)

demo.launch()