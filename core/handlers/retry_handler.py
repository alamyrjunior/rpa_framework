import time
import inspect
import os
from loguru import logger
from core.handlers.settings import Settings
from core.handlers.exception import BusinessException
from core.services.init import InitTask

default_retry = Settings().get("default_retry")

def retry(retries=default_retry, delay=2, exceptions=(Exception)):

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= retries:
                if attempts > 0:
                    logger.info(f"Realizando tentativa {attempts}")
                try:
                    return func(*args, **kwargs)
                except BusinessException as e:
                    # Se for uma exceção de negócio, loga e não faz retry
                    logger.error(f"Erro de negócio: {str(e)}. Não será feita nova tentativa.")
                    return None  # Não tenta novamente e continua o fluxo
                except exceptions as e:
                    if attempts == retries:
                        frame = inspect.currentframe()
                        outer_frames = inspect.getouterframes(frame)
                        caller_frame = outer_frames[1]
                        filename = caller_frame.filename
                        relative_path = os.path.relpath(filename)
                        relative_path_no_ext = os.path.splitext(relative_path)[0].replace("\\",".")
                        function_name = caller_frame.function
                        logger.error(
                            f"Todas as {retries} tentativas falharam."
                        )
                        raise Exception(f"{relative_path_no_ext}:{function_name} - {e}")
                    attempts += 1
                    time.sleep(delay)

        return wrapper

    return decorator
