# Voice Pro V2

## Архитектура проекта

### Основные компоненты системы

#### 1. Базовый компонент (components/base_component.py)

```python
class BaseComponent:
    # Статические менеджеры - общие для всех компонентов
    _db_manager = DatabaseManager()
    _settings_manager = SettingsManager(_db_manager)
    _state_manager = StateManager()

    def __init__(self, shared_state, component_name):
        self.shared_state = shared_state
        self.component_name = component_name
```

Базовый компонент теперь:
- Содержит все менеджеры как статические поля
- Требует только shared_state и component_name при создании
- Предоставляет доступ к менеджерам через свойства

#### 2. Менеджеры (core/)

##### SharedState (core/shared_state.py)
- Отвечает за управление общими UI элементами Gradio
- Единственный менеджер, который нужно явно передавать в компоненты
- Пример: скрытые аудио файлы, общие элементы интерфейса
```python
silent_audio = shared_state.get_silent_audio()
```

##### StateManager (core/state_manager.py)
- Управляет глобальным состоянием приложения
- Доступен через BaseComponent
- Хранит общие данные (API ключи, настройки Gradio)
```python
api_key = self.state_manager.get_global_value('api_keys')
```

##### SettingsManager (core/settings_manager.py)
- Управляет сохранением настроек в базе данных
- Доступен через BaseComponent
- Разделяет настройки по имени компонента
```python
settings = self.settings_manager.load_settings(self.component_name)
```

#### 3. Логика настроек

##### BaseSettingsLogic (core/settings_logic.py)
- Базовая логика для работы с настройками
- Предоставляет общий функционал
- Использует SettingsManager из BaseComponent

### Создание нового компонента

```python
class NewComponent(BaseComponent):
    def __init__(self, shared_state, component_name="new_component"):
        super().__init__(shared_state, component_name)
        self.logic = NewComponentLogic(self.component_name, self.settings_manager)
```

### Использование в приложении

```python
def initialize_app():
    # Только shared_state нужен для инициализации
    shared_state = SharedState()
    return shared_state

def create_app(shared_state):
    # Создаем компоненты только с shared_state и именем
    component = NewComponent(shared_state, "component_name")
```

### Преимущества новой архитектуры

1. **Упрощенная инициализация**
   - Компонентам нужны только shared_state и имя
   - Менеджеры создаются автоматически
   - Меньше дублирования кода

2. **Единая точка создания менеджеров**
   - Все менеджеры создаются в BaseComponent
   - Гарантируется единственность экземпляров
   - Легко добавлять новые менеджеры

3. **Чистый интерфейс компонентов**
   - Минимум параметров при создании
   - Доступ к менеджерам через свойства
   - Понятная иерархия зависимостей

4. **Автоматическое разделение данных**
   - Настройки разделяются по имени компонента
   - Локальное состояние изолировано
   - Глобальное состояние доступно всем

5. **Гибкость в расширении**
   - Легко добавлять новые компоненты
   - Простое переиспользование логики
   - Чистая структура зависимостей

### Взаимодействие компонентов

1. **Общие UI элементы**
   - Доступ через shared_state
   - Централизованное управление
   - Переиспользование элементов

2. **Глобальные данные**
   - Доступ через state_manager
   - Общие настройки и API ключи
   - Разделение с другими компонентами

3. **Настройки компонента**
   - Автоматическое разделение по имени
   - Сохранение в базе данных
   - Изоляция между компонентами

### Заключение

Новая архитектура значительно упрощает создание и использование компонентов, при этом сохраняя все преимущества предыдущей версии. Статические менеджеры в BaseComponent обеспечивают единую точку доступа к общим ресурсам, а минимальный набор параметров при создании компонентов делает код чище и понятнее. Это позволяет легко масштабировать приложение и добавлять новый функционал, сохраняя чистоту и организованность кода.
