from typing import Dict, Type
from .base_layout import BaseLayout
from core.shared_state import SharedState

class LayoutManager:
    """Менеджер для централизованного управления layouts"""
    
    def __init__(self):
        self._layouts: Dict[str, BaseLayout] = {}
        
    def register_layout(self, name: str, layout_class: Type[BaseLayout], shared_state_class: Type[SharedState] = None):
        """Регистрация нового layout с опциональным shared state
        
        Args:
            name (str): Имя layout для регистрации
            layout_class (Type[BaseLayout]): Класс layout
            shared_state_class (Type[SharedState], optional): Класс shared state для инъекции
        """
        # Создаем инстанс shared state если предоставлен класс
        shared_state = None
        if shared_state_class:
            shared_state = shared_state_class()
            
        # Создаем layout с предоставленным shared state
        layout = layout_class(shared_state) if shared_state else layout_class()
        
        # Инициализируем layout
        layout.initialize()
        layout.setup_components()
        self._layouts[name] = layout
        
    def get_layout(self, name: str) -> BaseLayout:
        """Получение layout по имени"""
        if name not in self._layouts:
            raise KeyError(f"Layout '{name}' not found")
        return self._layouts[name]
    
    def render_layout(self, name: str):
        """Рендер layout по имени"""
        layout = self.get_layout(name)
        layout.render()