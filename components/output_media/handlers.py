from core.base_handler import BaseHandler

class OutputMediaHandlers(BaseHandler):
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        super().__init__(logic, ui_elements, shared_state, state_manager)

    def bind_handlers(self):
        studio_import_video = self.export_manager.get_element("input_media_studio","input_media")

        studio_import_video.change(fn=self.logic.update_output_media, inputs=[studio_import_video], outputs=[self.ui_elements['output_media']])

