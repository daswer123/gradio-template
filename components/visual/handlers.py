from core.export_manager import ExportManager

class VisualHandlers:
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        self.logic = logic
        self.ui_elements = ui_elements
        self.shared_state = shared_state  # Для общих Gradio элементов
        self.state_manager = state_manager  # Для глобального состояния
        self.local_state = self.state_manager.get_local_state()  # Для локального состояния
        self.export_manager = ExportManager()  # Для доступа к элементам других компонентов
    
    def bind_handlers(self):
        """Пример как использовать элементы из settings компонента"""
        
        # Получаем элементы из settings компонента
        settings_volume = self.export_manager.get_element('settings', 'volume')
        settings_format = self.export_manager.get_element('settings', 'output_format')
        
        def update_visual_preview(volume_value):
            # Пример обработки изменения громкости из settings
            # Обновляем визуальное отображение громкости
            return f"Current volume: {volume_value}"
        
        def update_format_info(format_value):
            # Пример обработки изменения формата из settings
            return f"Selected format: {format_value}"
            
        # Привязываем обработчики к изменениям элементов settings
        settings_volume.change(
            fn=update_visual_preview,
            inputs=[settings_volume],
            outputs=[self.ui_elements['volume_display']]
        )
        
        settings_format.change(
            fn=update_format_info,
            inputs=[settings_format],
            outputs=[self.ui_elements['format_info']]
        )
