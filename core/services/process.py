from core.handlers.exception import ExceptionHandler, BusinessException
from core.handlers.settings import Settings
from framework.process_transaction import process
from core.services.init import InitTask
from loguru import logger


class ProcessTask:
    def __init__(self, queue_manager, context):
        self.queue_manager = queue_manager
        self.config = Settings()
        self.context = context
        self_queue_status = []

    @ExceptionHandler.handle_exception
    def execute(self):
        transaction_number = 0
        while not self.queue_manager.is_empty():
            transaction_number += 1
            queue_item = self.queue_manager.get_item()
            queue_item["transaction_number"] = transaction_number
            logger.info(f"Processando: item {transaction_number}")
            retries = queue_item["retries"]
            max_retries = 2
            try:
                if retries > 0:
                    logger.info(f"Realizando tentativa {retries}")
                    init_task = InitTask(self.queue_manager, self.context)
                    init_task.execute(False)

                process(self.config, queue_item, self.context)
                queue_item["status"] = "success"
            except BusinessException as e:
                logger.error(
                    "Houve uma exceção de negócio, não haverá nova tentativa.", e
                )
            except Exception as e:
                queue_item["retries"] += 1
                queue_item["retries"]
                if retries <= max_retries:
                    logger.error(
                        f"Erro ao processar item {transaction_number}: {str(e)}"
                    )
                    self.queue_manager.add_item(queue_item)
                else:
                    raise
