import gradio as gr

class StateManager:
    """Handles global application state"""
    def __init__(self):
        self.global_state = gr.State({
            'api_keys': {},
            'gradio_settings': {},
            # Can be extended with other global settings
        })
    
    def get_global_state(self):
        """Get the global state that's shared across all components"""
        return self.global_state
    
    def get_local_state(self):
        """Get a new local state instance for component-specific data"""
        return gr.State({})

    def update_global_state(self, key, value):
        """Update a value in global state"""
        current = self.global_state.value
        current[key] = value
        self.global_state.value = current
        return self.global_state.value
    
    def get_global_value(self, key, default=None):
        """Get a value from global state"""
        return self.global_state.value.get(key, default)