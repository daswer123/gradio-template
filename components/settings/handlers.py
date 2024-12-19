class SettingsHandlers:
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        self.logic = logic
        self.ui_elements = ui_elements
        self.shared_state = shared_state  # Для общих Gradio элементов
        self.state_manager = state_manager  # Для глобального состояния
    
    def bind_handlers(self):
        # Получаем локальный стейт для этого компонента
        local_state = self.state_manager.get_local_state()
        
        def update_settings(volume, sample_rate, output_format, current_state):
            # Обновляем настройки через logic
            new_settings = self.logic.update_settings(volume, sample_rate, output_format)
            
            # Пример как можно использовать глобальный стейт если нужно
            # global_state = self.state_manager.get_global_state()
            # api_key = self.state_manager.get_global_value('api_keys', {}).get('some_api')
            
            return new_settings
        
        def update_some(volume):
            return volume
        
        # Привязываем один обработчик ко всем элементам


        # В конце каждого компонента добавляем обработчик
        # Который сохранит необходимые нам настройки в БД
        compotents_list = ["volume", "sample_rate", "output_format"]
        for component in compotents_list:
            self.ui_elements[component].change(
                fn=update_settings,
                inputs=[
                    self.ui_elements['volume'],
                    self.ui_elements['sample_rate'],
                    self.ui_elements['output_format'],
                    local_state
                    ],
                outputs=[local_state]
            )

        self.ui_elements['volume'].change(
            fn=update_some,
            inputs=[self.ui_elements['volume']],
            outputs=self.shared_state.get_some_var()
        )
