import gradio as gr

def create_output_media_ui(current_settings):
    ui_elements = {}

    with gr.Column():   
        ui_elements["output_media"] = gr.Video(label="Видео",interactive=False)
        ui_elements["output_audio"] = gr.Audio(label="Аудио",interactive=False)
        ui_elements["output_subs"] = gr.TextArea(label="Субтитры")
    
    return ui_elements