import gradio as gr

def create_settings_ui(current_settings):
    with gr.Column():
        gr.Markdown("### Настройки")
        
        volume = gr.Slider(
            minimum=0, maximum=2, 
            value=current_settings['volume'],
            label="Громкость"
        )
        sample_rate = gr.Number(
            value=current_settings['sample_rate'],
            label="Частота дискретизации"
        )
        output_format = gr.Dropdown(
            choices=['wav', 'mp3', 'ogg'],
            value=current_settings['output_format'],
            label="Формат вывода"
        )
        
        return volume, sample_rate, output_format