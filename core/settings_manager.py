from database.models import Settings


class SettingsManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def load_settings(self, component_name, defaults):
        result = {}
        with self.db_manager.get_session() as session:
            settings = session.query(Settings).filter(
                Settings.component == component_name
            ).all()
            
            settings_dict = {s.key: s.value for s in settings}
            
            for key, default_value in defaults.items():
                result[key] = settings_dict.get(key, default_value)
            
        return result

    def save_settings(self, component_name, settings_dict):
        with self.db_manager.get_session() as session:
            session.query(Settings).filter(
                Settings.component == component_name
            ).delete()
            
            for key, value in settings_dict.items():
                setting = Settings(
                    component=component_name,
                    key=key,
                    value=str(value)
                )
                session.add(setting)
            
            session.commit()