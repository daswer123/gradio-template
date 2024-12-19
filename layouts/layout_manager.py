from typing import Dict, Type
from .base_layout import BaseLayout

class LayoutManager:
    """Менеджер для централизованного управления layouts"""
    
    def __init__(self):
        self._layouts: Dict[str, BaseLayout] = {}
        
    def register_layout(self, name: str, layout_class: Type[BaseLayout]):
        """Регистрация нового layout"""
        layout = layout_class()
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