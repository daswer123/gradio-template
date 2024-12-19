import gradio as gr

def create_settings_ui(current_settings):
    ui_elements = {}
    
    with gr.Column():
        gr.Markdown("### Настройки")
        ui_elements['volume'] = gr.Slider(
            minimum=0, maximum=2,
            value=current_settings['volume'],
            label="Громкость"
        )
        ui_elements['sample_rate'] = gr.Number(
            value=current_settings['sample_rate'],
            label="Частота дискретизации"
        )
        ui_elements['output_format'] = gr.Dropdown(
            choices=['wav', 'mp3', 'ogg'],
            value=current_settings['output_format'],
            label="Формат вывода"
        )
    
    return ui_elements