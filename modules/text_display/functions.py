# modules/text_display/functions.py
class TextDisplayFunctions:
    """Business logic for text display module"""
    
    @staticmethod
    def get_text_from_state(state, source_modules):
        """
        Get text from state for specified source modules
        Args:
            state: Application state
            source_modules: List of source module IDs
        Returns:
            Current text and status message
        """
        for source in source_modules:
            data = state.get(f"text_processor_{source}")
            if data and data.get("current_text"):
                return {
                    "text": data["current_text"],
                    "status": f"Updated from {source}"
                }
        
        return {
            "text": "No data",
            "status": "No data available"
        }

    @staticmethod
    def format_status_message(source_modules):
        """
        Format status message
        Args:
            source_modules: List of source module IDs
        Returns:
            Formatted status message
        """
        if not source_modules:
            return "No input sources connected"
        return f"Connected to: {', '.join(source_modules)}"