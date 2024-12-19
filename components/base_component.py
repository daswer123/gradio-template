from abc import ABC, abstractmethod
from database.database import DatabaseManager
from core.settings_manager import SettingsManager
from core.state_manager import StateManager
from core.export_manager import ExportManager

class BaseComponent(ABC):
    # Создаем статические менеджеры, которые будут общими для всех компонентов
    _db_manager = DatabaseManager()
    _db_manager.init_db()
    _settings_manager = SettingsManager(_db_manager)
    _state_manager = StateManager()
    _export_manager = ExportManager()

    def __init__(self, shared_state, component_name):
        # Только shared_state и component_name нужны при создании
        self.shared_state = shared_state
        self.component_name = component_name
        self.ui_elements = {}

    @property
    def settings_manager(self):
        return self._settings_manager

    @property
    def state_manager(self):
        return self._state_manager
    
    @property
    def export_manager(self):
        return self._export_manager
    
    def register_ui_elements(self, elements):
        """Регистрация UI элементов в export manager"""
        self.ui_elements = elements
        self.export_manager.register_component(self.component_name, elements)
    
    @abstractmethod
    def setup(self):
        """Инициализация компонента"""
        pass