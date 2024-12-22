from framework.init_transaction import init_all_applications, add_to_queue 
from core.handlers.settings import Settings
from loguru import logger


class InitTask:
    def __init__(self, queue_manager, context):
        self.queue_manager = queue_manager
        self.config = Settings()
        self.context = context

    def execute(self, first_run):
        if first_run:
            create_items = self.config.get("create_items")
            clear_queue = self.config.get("clear_queue")
            if clear_queue:
                pass
            if create_items:
                # Adiciona itens na fila
                add_to_queue(self.queue_manager)
        init_all_applications(self.config, self.context)

        logger.info("Processo iniciado com sucesso.")
