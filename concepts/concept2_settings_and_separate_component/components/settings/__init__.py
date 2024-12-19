from .ui import create_settings_ui
from .handlers import bind_handlers
from .logic import prepare_settings

def create_settings_component(shared_state, settings_manager):
    # Получаем начальные настройки
    current_settings = prepare_settings(settings_manager)
    
    # Создаем UI компоненты
    components = create_settings_ui(current_settings)
    
    # Привязываем обработчики
    bind_handlers(components, shared_state, settings_manager)