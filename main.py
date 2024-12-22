from core.helpers.logger import Logger
from core.handlers.queue import QueueManager
from core.services.init import InitTask
from core.services.process import ProcessTask
from core.services.end import EndTask
from core.helpers.context import Context

if __name__ == "__main__":
    # Configuração do logger
    logger = Logger.setup_logger()

    logger.info("Iniciando o processo")

    # Inicializando o gerenciador de filas
    queue_manager = QueueManager()
    context = Context()

    # Tasks
    init_task = InitTask(queue_manager, context)
    process_task = ProcessTask(queue_manager, context)
    end_task = EndTask()

    # Flags para controlar o sucesso das tasks
    success = True


    # Executando as tasks
    try:
        init_task.execute(True)
    except Exception as e:
        logger.error(f"Erro não tratado durante a inicialização: {str(e)}")
        success = False  # Marca que houve erro
        logger.info("Processo concluído com falha")

    if success:
        try:
            process_task.execute()
        except Exception as e:
            logger.error(f"Erro não tratado durante o processamento: {str(e)}")
            success = False  # Marca que houve erro

    # Independentemente de sucesso ou falha nas tasks anteriores, sempre executa o EndTask
    try:
        end_task.execute()
        if success:
            logger.info("Processo concluído com sucesso")
    except Exception as e:
        logger.error(f"Erro ao encerrar o processo: {str(e)}")
        success = False  # Marca que houve erro

    # Mensagem final
    if not success:
        logger.info("Processo concluído com falha")
