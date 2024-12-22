import queue

class QueueManager:
    def __init__(self):
        self.queue = queue.Queue()

    def add_item(self, item):
        """Adiciona um item à fila, garantindo que as chaves tenham os tipos esperados."""
        if not isinstance(item, dict):
            raise ValueError("O item precisa ser um dicionário.")
        
        # Garantindo que as chaves tenham os tipos esperados ou valores padrão
        for key, default_value in {
            'transaction_number': 0,  # valor padrão se não existir
            'retries': 0,  # valor padrão se não existir
            'reference': '',  # valor padrão se não existir
            'status': '',  # valor padrão se não existir
            'error_message': ''  # valor padrão se não existir
        }.items():
            if key not in item:
                item[key] = default_value
            elif isinstance(item[key], type(default_value)) is False:
                raise TypeError(f"A chave '{key}' deve ser do tipo '{type(default_value).__name__}'.")
        
        self.queue.put(item)

    def get_item(self):
        """Obtém o item da fila."""
        if not self.queue.empty():
            return self.queue.get()
        return None  # Retorna None se a fila estiver vazia

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return self.queue.empty()
