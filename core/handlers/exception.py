from loguru import logger

class BusinessException(Exception):
    """Exceção personalizada para regras de negócio."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ExceptionHandler:
    @staticmethod
    def handle_exception(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BusinessException as e:
                # Se for uma exceção de negócio, loga e continua para o próximo item
                logger.error(f"Erro de negócio: {str(e)}. Não será feita nova tentativa.")
                return None  # Não faz retry e continua o fluxo
            except Exception as e:
                # Loga os erros do sistema, que podem tentar o retry
                logger.error(f"Erro de sistema durante a execução: {str(e)}")
                raise  # Continua o fluxo mesmo após o erro
        return wrapper
