from typing import Dict, Any

class ExportManager:
    """Менеджер для экспорта Gradio элементов в глобальный стейт"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._components = {}
        return cls._instance
    
    def register_component(self, component_name: str, elements: Dict[str, Any]):
        """Регистрация Gradio элементов компонента в глобальном стейте
        
        Args:
            component_name (str): Имя компонента (например 'settings', 'visual')
            elements (Dict[str, Any]): Словарь Gradio элементов компонента
        """
        self._components[component_name] = elements
    
    def get_element(self, component_name: str, element_name: str) -> Any:
        """Получение Gradio элемента по имени компонента и элемента
        
        Args:
            component_name (str): Имя компонента (например 'settings')
            element_name (str): Имя элемента в компоненте (например 'volume')
            
        Returns:
            Any: Gradio элемент
            
        Raises:
            KeyError: Если компонент или элемент не найден
        """
        if component_name not in self._components:
            raise KeyError(f"Component '{component_name}' not found in export manager")
            
        component = self._components[component_name]
        if element_name not in component:
            raise KeyError(f"Element '{element_name}' not found in component '{component_name}'")
            
        return component[element_name]
    
    def get_component(self, component_name: str) -> Dict[str, Any]:
        """Получение всех элементов компонента
        
        Args:
            component_name (str): Имя компонента
            
        Returns:
            Dict[str, Any]: Словарь всех Gradio элементов компонента
            
        Raises:
            KeyError: Если компонент не найден
        """
        if component_name not in self._components:
            raise KeyError(f"Component '{component_name}' not found in export manager")
        return self._components[component_name]