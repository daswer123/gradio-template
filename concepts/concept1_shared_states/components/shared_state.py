import gradio as gr

class SharedState:
    def __init__(self):
        self.silent_audio = gr.File(label="Silent Audio", type="filepath", visible=True)
        
    def get_silent_audio(self):
        return self.silent_audio
    
