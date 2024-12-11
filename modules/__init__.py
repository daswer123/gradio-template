# modules/__init__.py
from .text_processor_simple import TextProcessor
from .text_display import TextDisplay
from .test_loader import TextLoader

MODULES = {
    "proc1": lambda state: TextProcessor(state, "proc1"),
    "display1": lambda state: TextDisplay(state, "display1"),
    "loader1": lambda state: TextLoader(state, "loader1"),
}