# modules/text_display/base.py
from ..base import BaseModule
from .ui import TextDisplayUI
from .handlers import TextDisplayHandlers
from .functions import TextDisplayFunctions

class TextDisplay(BaseModule):
    """Text display module with advanced functionality"""
    
    def __init__(self, state, module_id):
        """
        Initialize text display module
        Args:
            state: Application state instance
            module_id: Module identifier
        """
        super().__init__(state)
        self.module_id = module_id
        self.ui = TextDisplayUI(module_id)
        self.funcs = TextDisplayFunctions()
        self.handlers = TextDisplayHandlers(state, module_id, self.funcs)
        self.logger.debug(f"Initialized TextDisplay: {module_id}")
    
    def create_interface(self):
        """Create module interface with display components"""
        self.logger.debug("Creating interface")
        self.components = self.ui.create()
        self._register_components()
        self.logger.debug("Interface created")
    
    def setup_logic(self):
        """Setup module logic and event handlers"""
        self.logger.debug("Setting up logic")
        self.handlers.setup(self.components)
        self.logger.debug("Logic setup completed")