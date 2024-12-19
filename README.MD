# Gradio Template

A modular and scalable application architecture for Gradio-based applications.

## Features

- 🏗️ **Modular Architecture**
  - Component-based design
  - Reusable layouts
  - Clean separation of concerns

- 🎨 **Flexible UI Management**
  - Centralized layout management
  - Easy tab organization
  - Nested layouts support

- 🔄 **State Management**
  - Global and local states
  - Shared Gradio elements
  - Persistent settings

## Architecture Overview

### Core Components

#### 1. Layout System
- **BaseLayout**: Foundation for all layouts
- **LayoutManager**: Centralized layout management
- **Custom Layouts**: Modular UI sections

#### 2. State Management
- **SharedState**: Shared Gradio elements
- **StateManager**: Global application state
- **SettingsManager**: Persistent settings

#### 3. Component System
- **BaseComponent**: Foundation for all components
- **Static Managers**: Shared resources
- **Component Isolation**: Independent functionality

## Usage

### Creating a New Layout

```python
class CustomLayout(BaseLayout):
    def setup_components(self):
        self.components['custom'] = CustomComponent(
            self.shared_state, 
            "custom"
        )
    
    def render(self):
        with gr.Column():
            self.components['custom'].setup()
```

### Registering Layouts

```python
# Create layout manager
layout_manager = LayoutManager()

# Register layouts
layout_manager.register_layout('custom', CustomLayout)
```

### Building Interface

```python
with gr.Blocks() as demo:
    with gr.Tab("Custom"):
        layout_manager.render_layout('custom')
```

## Component Development

### Creating Components

```python
class CustomComponent(BaseComponent):
    def __init__(self, shared_state, component_name):
        super().__init__(shared_state, component_name)
        
    def setup(self):
        # Component UI setup
        pass
```

### Using Shared State

```python
# In SharedState
def initialize_elements(self):
    element = gr.Element(...)
    self.register_element('element', element)

# In Component
element = self.shared_state.get_element('element')
```

## Advanced Features

### State Management

- **Global State**: Application-wide data
- **Local State**: Component-specific data
- **Persistent Settings**: Database-backed configuration

### Layout Nesting

- Layouts can be nested within other layouts
- Flexible UI organization
- Reusable UI sections

### Component Communication

- Through shared state
- Via global state
- Using settings

## Best Practices

1. **Layout Organization**
   - One layout per logical UI section
   - Clear component ownership
   - Minimal dependencies

2. **State Management**
   - Use shared state for UI elements
   - Global state for app-wide data
   - Local state for component data

3. **Component Design**
   - Single responsibility
   - Clear interfaces
   - Independent functionality

4. **Code Structure**
   - Organized by feature
   - Clear file naming
   - Logical grouping

## Project Structure

```
project/
├── core/
│   ├── shared_state/
│   │   ├── base_shared_state.py
│   │   └── main_shared_state.py
│   ├── settings_manager.py
│   └── state_manager.py
├── components/
│   ├── base_component.py
│   └── custom/
├── layouts/
│   ├── base_layout.py
│   ├── layout_manager.py
│   └── custom/
└── app.py
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
