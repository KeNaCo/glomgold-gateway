from abc import ABC, abstractmethod

from acquiring.domain.payment import Payment


class Processor(ABC):
    @abstractmethod
    def process(self, payment: Payment):
        raise NotImplementedError()
