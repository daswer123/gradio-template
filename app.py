# app.py
import gradio as gr
from utils.logger import Logger, LogLevel
from app_configuration.state import State
from modules import MODULES
from app_configuration.app_config import AppConfig, AppInitializer

# =============================================
# Module Connections Configuration (Edit here)
# =============================================

class Application:
    def __init__(self,connections):
        self._init_components(connections)
        
    
    def _init_components(self,connections):
        """Initialize all core components"""
        try:
            self.logger = Logger("Application")
            
            self.config = AppConfig()
            self.state = State()
            initializer = AppInitializer(self.state)
            
            self.connection_manager = initializer.init_core()
            self.modules = initializer.init_modules(MODULES)
            
            self.connections = connections
            
            self.logger.info("Application initialized successfully")
        except Exception as e:
            self.logger.error(f"Initialization failed: {str(e)}")
            raise

    def create_interface(self):
        """Create the Gradio interface with all UI components"""
        settings = self.state.get_all_settings()
        
        with gr.Blocks(theme=settings["THEME"]) as interface:
            gr.Markdown(f"# {self.config.TITLE}")
            
            # =============================================
            # UI Configuration (Edit this section)
            # =============================================
            with gr.Tab("Text Processing"):
                try:
                    self.modules["proc1"].create_interface()
                    self.modules["display1"].create_interface()
                    self.logger.debug("Created Text Processing interface")
                except Exception as e:
                    self.logger.error(f"Failed to create interface: {str(e)}")
            with gr.Tab("Text Loader"):  # Добавляем новую вкладку
                try:
                    self.modules["loader1"].create_interface()
                    self.logger.debug("Created Text Loader interface")
                except Exception as e:
                    self.logger.error(f"Failed to create loader interface: {str(e)}")
            
            # Add more tabs and UI components here
            
            # =============================================
            # End of UI Configuration
            # =============================================
            
            self._setup_module_connections()
            self._setup_module_logic()
        
        return interface

    def _setup_module_connections(self):
        """Setup all configured module connections"""
        try:
            for source_id, target_id, target_component in self.connections:
                self.connection_manager.add_connection(
                    source_id=source_id,
                    target_id=target_id,
                    target_component=target_component
                )
            
            self.connection_manager.setup_connections()
            self.logger.info("Module connections setup completed")
        except Exception as e:
            self.logger.error(f"Failed to setup connections: {str(e)}")
            raise

    def _setup_module_logic(self):
        """Setup logic for all modules"""
        try:
            for module_id, module in self.modules.items():
                module.setup_logic()
                self.logger.debug(f"Logic setup completed for {module_id}")
        except Exception as e:
            self.logger.error(f"Failed to setup module logic: {str(e)}")
            raise

    def run(self):
        """Run the application"""
        try:
            interface = self.create_interface()
            settings = self.state.get_all_settings()
            
            self.logger.info("Starting application...")
            interface.launch(
                debug=settings["DEBUG"],
                share=settings["SHARE"],
                inbrowser=settings["INBROWSER"],
                server_name=settings["HOST"],
                server_port=settings["PORT"]
            )
        except Exception as e:
            self.logger.error(f"Failed to start application: {str(e)}")
            raise

def main():
    """Application entry point"""
    logger = Logger("Main")
    try:
        
        # EDIT CONNECTIONS HERE
        MODULE_CONNECTIONS = [
            ("proc1", "display1", "display_text"),
            # ("proc2", "display2", "display_text"),
        ]
        
        # END
        app = Application(MODULE_CONNECTIONS)
        app.run()
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        raise

if __name__ == "__main__":
    main()