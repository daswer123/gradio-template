# modules/test_loader.py
import gradio as gr
from utils.logger import Logger
from .base import BaseModule
import asyncio
import time

class TextLoader(BaseModule):
    def __init__(self, state, module_id: str):
        super().__init__(state)
        self.module_id = module_id
        self.logger = Logger(f"TextLoader_{module_id}")
        self.is_processing = False
        self.should_stop = False

    def create_interface(self):
        """Create module interface"""
        with gr.Row():
            self.components["input_text"] = gr.Textbox(
                label="Введите текст",
                placeholder="Текст для преобразования..."
            )

        with gr.Row():
            self.components["start_button"] = gr.Button("Начать обработку")
            self.components["stop_button"] = gr.Button("Остановить")

        with gr.Row():
            self.components["progress_info"] = gr.Label(label="Прогресс")
            
        with gr.Row():
            self.components["output_text"] = gr.Textbox(
                label="Результат",
                interactive=False
            )

        return self.components

    async def process_text(self, text: str, progress=gr.Progress()) -> str:
        """Process text with character-by-character progress"""
        if not text:
            return "Пожалуйста, введите текст"

        self.is_processing = True
        self.should_stop = False
        result = ""
        total_chars = len(text)

        try:
            # Начальное состояние
            progress(0, desc="Подготовка...")
            await asyncio.sleep(1)  # Небольшая задержка для отображения начального состояния

            # Обработка посимвольно
            for i in range(total_chars):
                if self.should_stop:
                    return "Обработка прервана пользователем"

                result += "0"  # Заменяем символ на "0"
                
                # Обновляем прогресс
                progress((i + 1) / total_chars, 
                        desc=f"Обработано {i + 1} из {total_chars} символов")
                
                await asyncio.sleep(3)  # Имитация обработки

            return result

        finally:
            self.is_processing = False

    def setup_logic(self):
        """Setup module logic"""
        async def start_processing(text: str, progress=gr.Progress()):
            if self.is_processing:
                return "Обработка уже идёт"
            return await self.process_text(text, progress)

        def stop_processing():
            if self.is_processing:
                self.should_stop = True
                return "Останавливаем обработку..."
            return "Нет активной обработки"

        # Привязываем обработчики событий
        self.components["start_button"].click(
            fn=start_processing,
            inputs=[self.components["input_text"]],
            outputs=[self.components["output_text"]]
        )

        self.components["stop_button"].click(
            fn=stop_processing,
            inputs=[],
            outputs=[self.components["progress_info"]]
        )

        # Добавляем обработку при прямом вводе текста
        self.components["input_text"].submit(
            fn=start_processing,
            inputs=[self.components["input_text"]],
            outputs=[self.components["output_text"]]
        )