from .logic import update_settings

def bind_handlers(components, shared_state, settings_manager):
    volume, sample_rate, output_format = components
    
    def handle_settings_update(volume, sample_rate, output_format, current_state):
        return update_settings(
            volume, 
            sample_rate, 
            output_format, 
            current_state, 
            settings_manager
        )

    # Привязка обработчиков
    for component in [volume, sample_rate, output_format]:
        component.change(
            fn=handle_settings_update,
            inputs=[volume, sample_rate, output_format, shared_state.get_settings_state()],
            outputs=[shared_state.get_settings_state()]
        )