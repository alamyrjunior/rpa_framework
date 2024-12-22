from loguru import logger


def kill_all_applications(config):
    pass


def ler_excel():
    return "excel"


def add_to_queue(queue_manager):
    logger.info("Estou aqui.")
    data = ler_excel()
    data = [
        {"nome": "Alamyr", "idade": 33},
        {"nome": "Tata", "idade": 27},
        {"nome": "Erley", "idade": 33},
        {},
    ]
    for item in data:
        queue_manager.add_item(item)


def init_all_applications(config, context):
    logger.info("Estou aqui no init all apps.")
