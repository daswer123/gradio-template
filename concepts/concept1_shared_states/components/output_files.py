import gradio as gr

def create_output_files_component(shared_state):
    with gr.Column():
        files = gr.Textbox(label="Files")
        
        # Можем добавить обработчик для взаимодействия с shared_state
        def handle_files_update(files):
            return str(files)
            
        files.change(fn=handle_files_update, inputs=files)

        shared_state.get_silent_audio().change(fn=handle_files_update, inputs=shared_state.get_silent_audio(),outputs=files)