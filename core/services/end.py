from core.handlers.settings import Settings
from framework.end_transaction import close_all_applications

class EndTask:
    def __init__(self):
        self.config = Settings()

    def execute(self):
        close_all_applications()
