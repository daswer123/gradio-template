from core.base_handler import BaseHandler

class SettingsHandlers(BaseHandler):
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        super().__init__(logic, ui_elements, shared_state, state_manager)
    
    def bind_handlers(self):
        # Получаем локальный стейт для этого компонента
        local_state = self.state_manager.get_local_state()
        
        def update_settings(youtube_quality, audio_format, current_state):
            # Обновляем настройки через logic
            new_settings = self.logic.update_settings(youtube_quality, audio_format)
            
            # Пример как можно использовать глобальный стейт если нужно
            # global_state = self.state_manager.get_global_state()
            # api_key = self.state_manager.get_global_value('api_keys', {}).get('some_api')
            
            return new_settings

        # В конце каждого компонента добавляем обработчик
        # Который сохранит необходимые нам настройки в БД
        compotents_list = ["youtube_quality", "audio_format"]

        # Привязываем обработчик к каждому элементу
        for component in compotents_list:
            self.ui_elements[component].change(
                fn=update_settings,
                inputs=[
                    self.ui_elements['youtube_quality'],
                    self.ui_elements['audio_format'],
                    local_state
                    ],
                outputs=[local_state]
            )

class InputMediaHandlers(BaseHandler):
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        super().__init__(logic, ui_elements, shared_state, state_manager)

    def bind_handlers(self):
        
        # Кнопка очистки
        self.ui_elements["clear_button"].click(
            fn=self.logic.clear_input_media,
            outputs=[self.ui_elements["input_media"], self.ui_elements["input_microphone"], self.ui_elements["input_youtube_url"]]
        )

        # Кнопка обработки
        print(self.export_manager._components)
        output_video = self.export_manager.get_element("output_media_studio","output_media")
        output_audio = self.export_manager.get_element("output_media_studio","output_audio")
        # output_files = self.export_manager.get_element("output_media_studio","output_subs")


        self.ui_elements["process_button"].click(
            fn=self.logic.process_input_media,
            inputs=[self.ui_elements["input_media"], self.ui_elements["input_microphone"], self.ui_elements["input_youtube_url"]],
            outputs=[output_video, output_audio]
        )

