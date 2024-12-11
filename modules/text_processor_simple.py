# modules/text_processor.py
import gradio as gr
from .base import BaseModule

class TextProcessorUI:
    """UI components for text processor"""
    
    def __init__(self, module_id: str):
        self.module_id = module_id
        self.components = {}
    
    def create(self):
        """Create UI components"""
        with gr.Row():
            self.components["input_text"] = gr.Textbox(
                label=f"Input Text ({self.module_id})",
                placeholder="Enter text to process...",
                interactive=True
            )
            self.components["process_button"] = gr.Button(
                value="Process",
                variant="primary"
            )
            self.components["output_text"] = gr.Textbox(
                label=f"Output ({self.module_id})",
                interactive=False
            )
        return self.components

class TextProcessorFunctions:
    """Business logic for text processor"""
    
    @staticmethod
    def process_text(text: str) -> str:
        """
        Process input text
        Args:
            text: Input text
        Returns:
            Processed text
        """
        return text.upper()

class TextProcessorHandlers:
    """Event handlers for text processor"""
    
    def __init__(self, state, module_id: str, functions):
        self.state = state
        self.module_id = module_id
        self.funcs = functions
    
    def setup(self, components):
        """Setup event handlers"""
        # Get target components from connection manager
        connection_manager = self.state.connection_manager
        target_components = connection_manager.get_module_outputs(self.module_id)
        
        # Define outputs: own output + connected components
        all_outputs = [components["output_text"]] + target_components
        
        # Setup click handler
        components["process_button"].click(
            fn=self.process_text_handler,
            inputs=[components["input_text"]],
            outputs=all_outputs
        )
    
    def process_text_handler(self, text: str) -> list:
        """
        Handle text processing
        Args:
            text: Input text
        Returns:
            List of processed text for all output components
        """
        # Process text
        processed = self.funcs.process_text(text)
        
        # Update state
        self.state.update(f"text_processor_{self.module_id}", {
            "current_text": processed,
            "last_updated": "now"
        })
        
        # Return processed text for all outputs
        output_count = len(self.state.connection_manager.get_module_outputs(self.module_id)) + 1
        return [processed] * output_count

class TextProcessor(BaseModule):
    """Text processor module"""
    
    def __init__(self, state, module_id: str):
        super().__init__(state)
        self.module_id = module_id
        self.ui = TextProcessorUI(module_id)
        self.funcs = TextProcessorFunctions()
        self.handlers = TextProcessorHandlers(state, module_id, self.funcs)
        self.logger.debug(f"Initialized TextProcessor: {module_id}")
    
    def create_interface(self):
        """Create module interface"""
        self.logger.debug("Creating interface")
        self.components = self.ui.create()
        self._register_components()
        self.logger.debug("Interface created")
    
    def setup_logic(self):
        """Setup module logic"""
        self.logger.debug("Setting up logic")
        self.handlers.setup(self.components)
        self.logger.debug("Logic setup completed")