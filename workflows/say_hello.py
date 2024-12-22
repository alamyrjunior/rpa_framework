from loguru import logger
def say_hello(nome, idade):
    logger.info(f"A idade de {nome} é {idade}")