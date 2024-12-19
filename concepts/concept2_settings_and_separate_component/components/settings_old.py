import gradio as gr

def create_settings_component(shared_state,settings_manager):
    def update_settings(volume, sample_rate, output_format, current_state):
        new_settings = {
            'volume': volume,
            'sample_rate': sample_rate,
            'output_format': output_format
        }
        
        # Валидируем и сохраняем настройки через менеджер
        # validated_settings = settings_manager.validate_settings(new_settings)
        settings_manager.save_settings(new_settings)
        return new_settings

    with gr.Column():
        gr.Markdown("### Настройки")
        
        current_settings = settings_manager.load_settings()
        
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

        # Обработчики изменений
        for component in [volume, sample_rate, output_format]:
            component.change(
                fn=update_settings,
                inputs=[volume, sample_rate, output_format, shared_state.get_settings_state()],
                outputs=[shared_state.get_settings_state()]
            )