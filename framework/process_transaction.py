from core.handlers.retry_handler import retry
from core.handlers.exception import BusinessException
from workflows.say_hello import say_hello

from loguru import logger


def process(config, queue_item, context):

    nome = queue_item["nome"]
    idade = queue_item["idade"]
    say_hello(nome, idade)
 
    if queue_item.get("transaction_number") == 1: 
        raise BusinessException("A transaction number is four")

    logger.info("Item processado com sucesso.")
