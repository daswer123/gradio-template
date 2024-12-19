import gradio as gr

def create_input_audio_component(shared_state):
    def process_audio(audio_input):
        # Можем использовать shared_state.silent_audio здесь
        return audio_input
    
    def process_shared_audio(audio_output):
        return audio_output
    
    with gr.Column():
        gr.Markdown("Мы что-то делаем с аудио.")
        with gr.Column():
            audio_input = gr.Audio(label="Input Audio", type="filepath")
        
        audio_output = gr.Audio(label="Output Audio", interactive=False, type="filepath")
        btn = gr.Button("Run")
        
        btn.click(fn=process_audio, inputs=audio_input, outputs=[audio_output])
        audio_output.change(fn=process_shared_audio, inputs=audio_output, outputs=shared_state.get_silent_audio())

        