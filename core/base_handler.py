from core.export_manager import ExportManager

class BaseHandler:
    def __init__(self, logic, ui_elements, shared_state, state_manager):
        self.logic = logic
        self.ui_elements = ui_elements
        self.shared_state = shared_state  # Для общих Gradio элементов
        self.state_manager = state_manager  # Для глобального состояния
        self.export_manager = ExportManager()

    def bind_handlers(self):
        pass

