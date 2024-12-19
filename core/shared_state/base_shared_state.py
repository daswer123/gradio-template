import gradio as gr
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseSharedState(ABC):
    """Базовый класс для всех SharedState с общей функциональностью"""
    
    def __init__(self):
        self._elements: Dict[str, Any] = {}
        self.initialize_elements()
    
    @abstractmethod
    def initialize_elements(self):
        """Инициализация Gradio элементов для конкретного SharedState"""
        pass
    
    def register_element(self, name: str, element: Any):
        """Регистрация Gradio элемента"""
        self._elements[name] = element
    
    def get_element(self, name: str) -> Any:
        """Получение Gradio элемента по имени"""
        if name not in self._elements:
            raise KeyError(f"Element '{name}' not found in shared state")
        return self._elements[name]
    
    def get_all_elements(self) -> Dict[str, Any]:
        """Получение всех зарегистрированных элементов"""
        return self._elements.copy()