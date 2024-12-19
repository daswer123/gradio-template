# Voice Pro V2

## Архитектура проекта

### Основные компоненты системы

#### 1. Layout Manager (layouts/layout_manager.py)

```python
class LayoutManager:
    def __init__(self):
        self._layouts = {}
    
    def register_layout(self, name: str, layout_class: Type[BaseLayout]):
        layout = layout_class()
        layout.initialize()
        layout.setup_components()
        self._layouts[name] = layout
    
    def render_layout(self, name: str):
        layout = self.get_layout(name)
        layout.render()
```

Менеджер layouts:
- Централизованное управление layouts
- Автоматическая инициализация
- Простое добавление новых layouts

#### 2. Layouts (layouts/)

##### BaseLayout (layouts/base_layout.py)
```python
class BaseLayout:
    def __init__(self):
        self.shared_state = None
        self.components = {}
    
    def render(self):
        """Рендер layout - переопределяется в наследниках"""
        pass
```

##### Пример Layout'а
```python
class SettingsLayout(BaseLayout):
    def setup_components(self):
        self.components['settings'] = SettingsComponent(
            self.shared_state, 
            "settings"
        )
    
    def render(self):
        with gr.Column():
            self.components['settings'].setup()
```

#### 3. Shared States (core/shared_state/)

##### BaseSharedState (core/shared_state/base_shared_state.py)
```python
class BaseSharedState:
    def __init__(self):
        self._elements = {}
        self.initialize_elements()
    
    def register_element(self, name: str, element: Any):
        self._elements[name] = element
```

#### 4. Компоненты (components/)

##### BaseComponent (components/base_component.py)
```python
class BaseComponent:
    _db_manager = DatabaseManager()
    _settings_manager = SettingsManager(_db_manager)
    _state_manager = StateManager()

    def __init__(self, shared_state, component_name):
        self.shared_state = shared_state
        self.component_name = component_name
```

### Использование Layout Manager

#### Регистрация layouts
```python
# Создаем менеджер
layout_manager = LayoutManager()

# Регистрируем layouts
layout_manager.register_layout('settings', SettingsLayout)
layout_manager.register_layout('audio', AudioLayout)
layout_manager.register_layout('video', VideoLayout)
```

#### Создание интерфейса
```python
with gr.Blocks() as demo:
    with gr.Tab("Settings"):
        layout_manager.render_layout('settings')
    with gr.Tab("Audio"):
        layout_manager.render_layout('audio')
    with gr.Tab("Video"):
        layout_manager.render_layout('video')
```

### Преимущества новой архитектуры

1. **Централизованное управление**
   - Единая точка управления layouts
   - Автоматическая инициализация
   - Простое добавление новых layouts

2. **Чистый код**
   - Меньше повторяющегося кода
   - Понятная структура приложения
   - Легкое масштабирование

3. **Гибкость**
   - Простое добавление новых layouts
   - Легкая компоновка интерфейса
   - Переиспользование layouts

4. **Организация**
   - Четкое разделение ответственности
   - Управляемые зависимости
   - Легкое тестирование

### Создание нового Layout'а

1. Создать класс layout'а:
```python
class NewLayout(BaseLayout):
    def setup_components(self):
        # Настройка компонентов
        pass
    
    def render(self):
        # Рендер интерфейса
        pass
```

2. Зарегистрировать в менеджере:
```python
layout_manager.register_layout('new', NewLayout)
```

3. Использовать в интерфейсе:
```python
with gr.Tab("New"):
    layout_manager.render_layout('new')
```

### Заключение

Новая архитектура с LayoutManager значительно упрощает управление layouts и делает код более организованным. Централизованное управление через менеджер уменьшает дублирование кода и упрощает добавление новых функциональностей. Это делает приложение более масштабируемым и легким в поддержке.
