# utils/database.py
import sqlite3
import os
from pathlib import Path
from typing import Dict, Optional

class Database:
    def __init__(self, db_path: str = "user.db"):
        self.db_path = db_path
        self._ensure_dir_exists()
        self._init_db()
    
    def _ensure_dir_exists(self):
        Path(os.path.dirname(self.db_path)).mkdir(parents=True, exist_ok=True)
    
    def _init_db(self):
        is_new_db = not os.path.exists(self.db_path)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            """)
            
            if is_new_db:
                print(f"Created new database at: {self.db_path}")
    
    def set_setting(self, key: str, value: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO settings (key, value)
                VALUES (?, ?)
            """, (key, str(value)))
    
    def get_settings(self) -> Dict[str, str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT key, value FROM settings")
            return dict(cursor.fetchall())
    
    def clear_settings(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM settings")