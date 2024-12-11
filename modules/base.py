# modules/base.py
from abc import ABC, abstractmethod
from utils.logger import Logger

class BaseModule(ABC):
    """Base class for all modules"""
    
    def __init__(self, state):
        """
        Initialize base module
        Args:
            state: Application state instance
        """
        try:
            self.state = state
            self.components = {}
            self.module_id = None
            self.logger = Logger(f"Module_{self.module_id or 'Base'}")
            self.logger.debug("Base module initialized")
        except Exception as e:
            self.logger.error(f"Failed to initialize base module: {str(e)}")
            raise

    def _register_components(self):
        """Auto-register all components that should be available to other modules"""
        try:
            registered_count = 0
            for name, component in self.components.items():
                if 'output' in name or 'display' in name:
                    try:
                        component_id = f"{self.module_id}_{name}"
                        self.state.register_component(component_id, component)
                        self.logger.debug(f"Registered component: {component_id}")
                        registered_count += 1
                    except Exception as e:
                        self.logger.error(f"Failed to register component {name}: {str(e)}")
            
            self.logger.debug(f"Registered {registered_count} components")
                        
        except Exception as e:
            self.logger.error(f"Failed to register components: {str(e)}")
            raise

    @abstractmethod
    def create_interface(self):
        """
        Create module interface
        This method should be implemented by derived classes
        """
        pass

    @abstractmethod
    def setup_logic(self):
        """
        Setup module logic and event handlers
        This method should be implemented by derived classes
        """
        pass