import gradio as gr

class SharedState:
    """Handles shared Gradio UI elements that need to be accessible across components"""
    def __init__(self):
        # Hidden Gradio elements that can be shared between components
        self.silent_audio = gr.File(label="Silent Audio", type="filepath", visible=False)
        # Add other shared Gradio elements as needed
        
    def get_silent_audio(self):
        return self.silent_audio
