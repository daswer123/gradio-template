# config/app_config.py
from dataclasses import dataclass
from utils.logger import Logger

@dataclass
class AppConfig:
    """Base application configuration containing core application settings"""
    TITLE = "Application"

class AppInitializer:
    """
    Handles basic application initialization including core components and modules.
    Responsible for setting up the application's foundational structure.
    """
    
    def __init__(self, state):
        """
        Initialize AppInitializer
        Args:
            state: Application state manager instance
        """
        self.state = state
        self.logger = Logger("AppInitializer")
        self.logger.debug("AppInitializer created")
    
    def init_core(self):
        """
        Initialize core components of the application.
        Creates and sets up essential services like connection manager.
        
        Returns:
            ModuleConnectionManager: Initialized connection manager instance
        
        Raises:
            Exception: If core initialization fails
        """
        self.logger.info("Starting core initialization")
        
        try:
            from modules.connection_manager import ModuleConnectionManager
            
            # Create and bind connection manager
            connection_manager = ModuleConnectionManager(self.state)
            self.state.connection_manager = connection_manager
            
            self.logger.info("Core components initialized successfully")
            return connection_manager
            
        except Exception as e:
            self.logger.error(f"Core initialization failed: {str(e)}")
            raise
    
    def init_modules(self, modules_config):
        """
        Initialize modules from configuration.
        Sets up all application modules and registers them with the connection manager.
        
        Args:
            modules_config: Dictionary mapping module names to their initializer functions
        
        Returns:
            dict: Dictionary of initialized module instances
        
        Raises:
            RuntimeError: If no modules could be initialized successfully
        """
        self.logger.info("Starting modules initialization")
        modules = {}
        
        # Initialize modules
        for name, module in modules_config.items():
            try:
                self.logger.debug(f"Initializing module: {name}")
                modules[name] = module(self.state)
                self.logger.debug(f"Successfully initialized module: {name}")
                
            except Exception as e:
                self.logger.error(f"Failed to initialize module {name}: {str(e)}")
                continue  # Continue with other modules even if one fails
        
        if not modules:
            self.logger.error("No modules were initialized successfully")
            raise RuntimeError("Failed to initialize any modules")
        
        # Register modules in connection manager
        self.logger.debug("Starting module registration")
        for module_id, module in modules.items():
            try:
                self.state.connection_manager.register_module(module_id, module)
                self.logger.debug(f"Registered module: {module_id}")
                
            except Exception as e:
                self.logger.error(f"Failed to register module {module_id}: {str(e)}")
        
        self.logger.info(f"Initialized and registered {len(modules)} modules")
        return modules