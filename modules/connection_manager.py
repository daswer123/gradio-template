# modules/connection_manager.py
from dataclasses import dataclass
from typing import Union, List
from utils.logger import Logger

@dataclass 
class ModuleConnection:
    """Data class for storing module connection information"""
    source_id: str
    target_id: str
    target_component: Union[str, List[str]]

class ModuleConnectionManager:
    """Manages connections between modules"""
    
    def __init__(self, state):
        """
        Initialize connection manager
        Args:
            state: Application state instance
        """
        self.state = state
        self.connections = []
        self.modules = {}
        self.logger = Logger("ConnectionManager")
        self.logger.debug("Initialized connection manager")

    def register_module(self, module_id: str, module):
        """
        Register a module in the connection manager
        Args:
            module_id: Module identifier
            module: Module instance
        """
        try:
            self.modules[module_id] = module
            self.logger.debug(f"Registered module: {module_id}")
        except Exception as e:
            self.logger.error(f"Failed to register module {module_id}: {str(e)}")
            raise

    def add_connection(self, source_id: str, target_id: str,
                      target_component: Union[str, List[str]] = "display_text"):
        """
        Add connection between modules
        Args:
            source_id: Source module ID
            target_id: Target module ID
            target_component: Target component(s) identifier
        """
        try:
            if isinstance(target_component, str):
                target_component = [target_component]
            
            connection = ModuleConnection(
                source_id=source_id,
                target_id=target_id,
                target_component=target_component
            )
            self.connections.append(connection)
            self.logger.debug(f"Added connection: {source_id} -> {target_id}:{target_component}")
        except Exception as e:
            self.logger.error(f"Failed to add connection {source_id}->{target_id}: {str(e)}")
            raise

    def setup_connections(self):
        """Setup all module connections"""
        self.logger.info("Starting connections setup")
        for connection in self.connections:
            try:
                source_module = self.modules[connection.source_id]
                target_module = self.modules[connection.target_id]
                
                for target_comp in connection.target_component:
                    if target_comp in target_module.components:
                        self.logger.debug(
                            f"Setup connection: {connection.source_id} -> {connection.target_id}:{target_comp}"
                        )
                    else:
                        self.logger.warning(
                            f"Component {target_comp} not found in {connection.target_id}"
                        )
            except KeyError as e:
                self.logger.error(f"Error setting up connection: Module not found - {str(e)}")

    def get_module_outputs(self, module_id: str) -> List:
        """
        Get output components for module
        Args:
            module_id: Module identifier
        Returns:
            List of output components
        """
        outputs = []
        try:
            for conn in self.connections:
                if conn.source_id == module_id:
                    target_module = self.modules[conn.target_id]
                    for target_comp in conn.target_component:
                        if target_comp in target_module.components:
                            outputs.append(target_module.components[target_comp])
                        else:
                            self.logger.warning(
                                f"Component {target_comp} not found in {conn.target_id}"
                            )
            self.logger.debug(f"Retrieved {len(outputs)} outputs for module {module_id}")
            return outputs
        except Exception as e:
            self.logger.error(f"Error getting outputs for module {module_id}: {str(e)}")
            return []

    def get_module_inputs(self, module_id: str) -> List[str]:
        """
        Get input module IDs for module
        Args:
            module_id: Module identifier
        Returns:
            List of input module IDs
        """
        try:
            inputs = [conn.source_id for conn in self.connections if conn.target_id == module_id]
            self.logger.debug(f"Retrieved {len(inputs)} inputs for module {module_id}")
            return inputs
        except Exception as e:
            self.logger.error(f"Error getting inputs for module {module_id}: {str(e)}")
            return []