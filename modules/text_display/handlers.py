# modules/text_display/handlers.py
class TextDisplayHandlers:
    """Event handlers for text display module"""
    
    def __init__(self, state, module_id, functions):
        self.state = state
        self.module_id = module_id
        self.funcs = functions
    
    def setup(self, components):
        """Setup event handlers"""
        # Get source modules
        connection_manager = self.state.connection_manager
        source_modules = connection_manager.get_module_inputs(self.module_id)
        
        # Update initial status
        components["status_text"].value = self.funcs.format_status_message(source_modules)
        
        # Setup refresh handler
        def refresh_handler():
            result = self.funcs.get_text_from_state(self.state, source_modules)
            return [
                result["text"],
                result["status"]
            ]
        
        components["refresh_button"].click(
            fn=refresh_handler,
            inputs=[],
            outputs=[
                components["display_text"],
                components["status_text"]
            ]
        )