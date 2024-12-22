from loguru import logger
from core.handlers.settings import Settings
from datetime import datetime

class Logger:
    @staticmethod
    def setup_logger():
        timestamp= datetime.now().strftime("%Y%m%m_%H%M%S")
        settings = Settings()
        month = datetime.now().strftime("%b").lower()
        day = datetime.now().day
        project_name = str(settings.get("project_name", "RPA Framework")).replace(" ","_").lower()
        log_file = f"logs/{month}/{day}/{project_name}_{timestamp}.log"
        log_level = settings.get("log_level")
        
        logger.add(
            log_file,
            level=log_level,
            format="{time} - {level} - {message}",
            rotation="10 MB",
            retention="10 days",
            compression="zip",
        )
        return logger