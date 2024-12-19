def prepare_settings(settings_manager):
    """Подготовка настроек перед созданием UI"""
    return settings_manager.load_settings()

def update_settings(volume, sample_rate, output_format, current_state, settings_manager):
    """Обновление настроек"""
    new_settings = {
        'volume': volume,
        'sample_rate': sample_rate,
        'output_format': output_format
    }
    
    settings_manager.save_settings(new_settings)
    return new_settings