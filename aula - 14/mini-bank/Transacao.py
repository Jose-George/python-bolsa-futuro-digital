from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        """Deve retornar o valor da transação."""
        pass

    @abstractmethod
    def registrar(self, conta):
        """Deve registrar a transação na conta fornecida."""
        pass
