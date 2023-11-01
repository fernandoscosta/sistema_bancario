from abc import ABC, abstractproperty

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractproperty
    def registrar(self, conta):
        pass
