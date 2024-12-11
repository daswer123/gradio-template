# modules/text_display/ui.py
import gradio as gr

class TextDisplayUI:
    """UI components for text display module"""
    
    def __init__(self, module_id):
        self.module_id = module_id
        self.components = {}
    
    def create(self):
        """Create UI components"""
        with gr.Row():
            self.components["display_text"] = gr.Textbox(
                label=f"State Text ({self.module_id})",
                interactive=False,
                show_copy_button=True
            )
            self.components["refresh_button"] = gr.Button(
                value=f"Refresh {self.module_id}",
                variant="secondary"
            )
        
        with gr.Row():
            self.components["status_text"] = gr.Markdown(
                value="Ready to display"
            )
        
        return self.components